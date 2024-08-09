from dataclasses import dataclass, field
from typing import Dict, List, Optional

from greenbutton_objects.data.atom import ContentType, EntryType, Feed


@dataclass
class HRefTreeNode:
    uri: str
    parent: Optional[str] = None
    contentType: type = type(None)
    content: List[ContentType] = field(default_factory=list)
    children: List[str] = field(default_factory=list)
    related: List[str] = field(default_factory=list)
    title: str = ""


class HRefForest:
    def __init__(self) -> None:
        self.forest: Dict[str, HRefTreeNode] = {}

    def __ensure_container(self, uri: str) -> None:
        if uri not in self.forest:
            self.forest[uri] = HRefTreeNode(uri)

    def __link_parents(self) -> "HRefForest":
        for node in self.forest.values():
            if node.parent:
                parent_node = self.forest.get(node.parent)
                if parent_node:
                    parent_node.children.append(node.uri)
        return self

    def __ensure_containers(self) -> "HRefForest":
        for key in list(self.forest.keys()):
            node = self.forest[key]
            if node.parent:
                self.__ensure_container(node.parent)
            for related_uri in node.related:
                self.__ensure_container(related_uri)
        return self

    def __add_nodes(self, feed: Feed) -> "HRefForest":
        def entry_content_type(entry: EntryType) -> type:
            if entry.content and entry.content[0].content:
                content_type = type(entry.content[0].content[0])
            else:
                content_type = type(None)
            return content_type

        for entry in feed.entry:
            related = []
            parent = None
            uri = ""

            content_type = entry_content_type(entry)

            for link in entry.link:
                # Skip links without URIs
                if not link.href:
                    continue
                if link.rel == "self":
                    uri = link.href
                elif link.rel == "related":
                    related.append(link.href)
                elif link.rel == "up":
                    parent = link.href

            title = self.get_entry_title(entry)

            self.forest[uri] = HRefTreeNode(
                uri=uri,
                title=title,
                parent=parent,
                related=related,
                contentType=content_type,
                content=entry.content,
            )

        return self

    @staticmethod
    def get_entry_title(entry: EntryType) -> str:
        if entry.title:
            title_parts = []
            for text in entry.title:
                if len(text.content) > 0:
                    title_parts.append(text.content[0])
            return "".join(title_parts)  # type: ignore
        else:
            return ""

    def build(self, feed: Feed) -> "HRefForest":
        return self.__add_nodes(feed).__ensure_containers().__link_parents()

    def root_nodes(self) -> List[str]:
        return [node.uri for node in self.forest.values() if node.parent is None]
