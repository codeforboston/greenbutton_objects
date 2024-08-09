from typing import Iterable, Type, TypeVar, Union

T = TypeVar("T")
S = TypeVar("S")


def get_first(iterable: Iterable[T]) -> Union[T, None]:
    for item in iterable:
        return item
    return None


def get_value(source: S, missing_val: T, dest_type: Type[T], src_type: Type[S]) -> T:
    # TODO: See if we can get a generic type for dest_type and src_type
    #       generic type is something that has .value attribute
    #       also we should get a generic type of dest value which is something that can
    #       take and int or src_type as an argument for creation
    value: T = dest_type(missing_val.value)  # type: ignore
    if isinstance(source, int):
        value = dest_type(source)  # type: ignore
    elif isinstance(source, src_type):
        value = dest_type(source.value)  # type: ignore
    return value
