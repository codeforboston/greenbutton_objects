#!/usr/bin/python

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig

import greenbutton_objects.data.atom as atom
from greenbutton_objects.atom.entry_forest import EntryForest
from greenbutton_objects.atom.href_forest import HRefForest
from greenbutton_objects.feed.feed import ObjectFeed


def untested_function(filename: str) -> str:
    return filename.capitalize()


def parse_feed(filename: str) -> ObjectFeed:
    data = parse_xml(filename)

    href_forest = HRefForest().build(data)
    entry_forest = EntryForest().build(href_forest)
    object_feed = ObjectFeed().build(entry_forest)

    return object_feed


def parse_xml(filename: str) -> atom.Feed:
    data = get_xml_parser().parse(filename, clazz=atom.Feed)
    return data


def get_xml_parser() -> XmlParser:
    config = ParserConfig(fail_on_unknown_properties=False)
    context = XmlContext()
    return XmlParser(context=context, config=config)
