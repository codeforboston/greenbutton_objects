from dataclasses import dataclass, field
from itertools import chain
from typing import Any, Dict, Iterable, List, Optional, Sequence, Union

from greenbutton_objects.atom.href_forest import HRefForest, HRefTreeNode
from greenbutton_objects.util import get_first


@dataclass
class EntryNode:
    title: str
    uri: str
    content: Sequence[object]

    parent: Optional["EntryNode"] = None
    content_type: type = type(None)
    children_type: type = type(None)
    children: List["EntryNode"] = field(default_factory=list)
    # TODO: Should related be a list or dict keyed by type?
    related: List["EntryNode"] = field(default_factory=list)

    def infer_children_type(self) -> None:
        # We are making a big assumption here that all children are of the same type.
        # This is to make things simpler for the consumer who's using the library
        if self.children and self.children[0].content:
            content_ = self.children[0].content[0]
            if content_.content:  # type: ignore
                self.children_type = content_.content[0].__class__  # type: ignore
            else:
                self.children_type = type(None)

    def first_content(self) -> Any:
        first_node = get_first(self.content)
        first_node_content = first_node.content  # type: ignore
        return get_first(first_node_content)

    def get_related_of_type(self, elements_type: type) -> Iterable["EntryNode"]:
        containers = [obj for obj in self.related if obj.children_type is elements_type]
        if containers:
            elements: Iterable[EntryNode] = chain.from_iterable(
                container.children for container in containers
            )
        else:
            elements = [obj for obj in self.related if obj.content_type is elements_type]
        return elements

    def safe_get_content(self, content_type: type) -> Union[Any, None]:
        obj = get_first(self.get_related_of_type(content_type))
        return obj.first_content() if obj else None


class EntryForest:
    def __init__(
        self,
    ) -> None:
        self.__roots: List[EntryNode] = []

    def build(self, href_forest: HRefForest) -> "EntryForest":
        node_cache: Dict[str, EntryNode] = {}

        def add_node(href_node: HRefTreeNode) -> EntryNode:
            entry_node = EntryNode(
                title=href_node.title,
                uri=href_node.uri,
                content=href_node.content,
                content_type=href_node.contentType,
            )
            node_cache[href_node.uri] = entry_node
            return entry_node

        def build_tree(node_uri: str) -> EntryNode:
            if node_uri not in node_cache:
                href_node = href_forest.forest[node_uri]
                entry_node = add_node(href_node)

                # Children
                entry_node.children = [build_tree(child) for child in href_node.children]
                for child in entry_node.children:
                    child.parent = entry_node
                entry_node.infer_children_type()

                # Relatives
                entry_node.related = [build_tree(child) for child in href_node.related]

            return node_cache[node_uri]

        self.__roots = [build_tree(uri) for uri in href_forest.root_nodes()]

        return self

    @staticmethod
    def get_elements_by_type(elements_type: type, source: list[EntryNode]) -> Iterable[EntryNode]:
        containers = [obj for obj in source if obj.children_type is elements_type]
        if containers:
            elements: Iterable[EntryNode] = chain.from_iterable(
                container.children for container in containers
            )
        else:
            elements = [obj for obj in source if obj.content_type is elements_type]
        return elements

    @property
    def roots(self) -> List[EntryNode]:
        return self.__roots
