from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attribute_mapping_source_type import AttributeMappingSourceType
    from .string_key_attribute_mapping_source_value_pair import StringKeyAttributeMappingSourceValuePair

@dataclass
class AttributeMappingSource(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Equivalent expression representation of this attributeMappingSource object.
    expression: Optional[str] = None
    # Name parameter of the mapping source. Depending on the type property value, this can be the name of the function, the name of the source attribute, or a constant value to be used.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # If this object represents a function, lists function parameters. Parameters consist of attributeMappingSource objects themselves, allowing for complex expressions. If type isn't Function, this property is null/empty array.
    parameters: Optional[List[StringKeyAttributeMappingSourceValuePair]] = None
    # The type property
    type: Optional[AttributeMappingSourceType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttributeMappingSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AttributeMappingSource
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AttributeMappingSource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .attribute_mapping_source_type import AttributeMappingSourceType
        from .string_key_attribute_mapping_source_value_pair import StringKeyAttributeMappingSourceValuePair

        from .attribute_mapping_source_type import AttributeMappingSourceType
        from .string_key_attribute_mapping_source_value_pair import StringKeyAttributeMappingSourceValuePair

        fields: Dict[str, Callable[[Any], None]] = {
            "expression": lambda n : setattr(self, 'expression', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "parameters": lambda n : setattr(self, 'parameters', n.get_collection_of_object_values(StringKeyAttributeMappingSourceValuePair)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(AttributeMappingSourceType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("expression", self.expression)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("parameters", self.parameters)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

