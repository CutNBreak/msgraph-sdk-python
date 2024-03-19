from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_item import BaseItem
    from .page_layout_type import PageLayoutType
    from .publication_facet import PublicationFacet
    from .site_page import SitePage

from .base_item import BaseItem

@dataclass
class BaseSitePage(BaseItem):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.baseSitePage"
    # The pageLayout property
    page_layout: Optional[PageLayoutType] = None
    # The publishingState property
    publishing_state: Optional[PublicationFacet] = None
    # The title property
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BaseSitePage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BaseSitePage
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sitePage".casefold():
            from .site_page import SitePage

            return SitePage()
        return BaseSitePage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .base_item import BaseItem
        from .page_layout_type import PageLayoutType
        from .publication_facet import PublicationFacet
        from .site_page import SitePage

        from .base_item import BaseItem
        from .page_layout_type import PageLayoutType
        from .publication_facet import PublicationFacet
        from .site_page import SitePage

        fields: Dict[str, Callable[[Any], None]] = {
            "pageLayout": lambda n : setattr(self, 'page_layout', n.get_enum_value(PageLayoutType)),
            "publishingState": lambda n : setattr(self, 'publishing_state', n.get_object_value(PublicationFacet)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("pageLayout", self.page_layout)
        writer.write_object_value("publishingState", self.publishing_state)
        writer.write_str_value("title", self.title)
    

