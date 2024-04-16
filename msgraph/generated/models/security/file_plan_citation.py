from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .file_plan_descriptor_base import FilePlanDescriptorBase

from .file_plan_descriptor_base import FilePlanDescriptorBase

@dataclass
class FilePlanCitation(FilePlanDescriptorBase):
    # The citationJurisdiction property
    citation_jurisdiction: Optional[str] = None
    # The citationUrl property
    citation_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FilePlanCitation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilePlanCitation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return FilePlanCitation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .file_plan_descriptor_base import FilePlanDescriptorBase

        from .file_plan_descriptor_base import FilePlanDescriptorBase

        fields: Dict[str, Callable[[Any], None]] = {
            "citationJurisdiction": lambda n : setattr(self, 'citation_jurisdiction', n.get_str_value()),
            "citationUrl": lambda n : setattr(self, 'citation_url', n.get_str_value()),
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
        writer.write_str_value("citationJurisdiction", self.citation_jurisdiction)
        writer.write_str_value("citationUrl", self.citation_url)
    

