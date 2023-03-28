from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class SydPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new sydPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The cost property
        self._cost: Optional[json.Json] = None
        # The life property
        self._life: Optional[json.Json] = None
        # The per property
        self._per: Optional[json.Json] = None
        # The salvage property
        self._salvage: Optional[json.Json] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def cost(self,) -> Optional[json.Json]:
        """
        Gets the cost property value. The cost property
        Returns: Optional[json.Json]
        """
        return self._cost
    
    @cost.setter
    def cost(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the cost property value. The cost property
        Args:
            value: Value to set for the cost property.
        """
        self._cost = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SydPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SydPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SydPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "cost": lambda n : setattr(self, 'cost', n.get_object_value(json.Json)),
            "life": lambda n : setattr(self, 'life', n.get_object_value(json.Json)),
            "per": lambda n : setattr(self, 'per', n.get_object_value(json.Json)),
            "salvage": lambda n : setattr(self, 'salvage', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def life(self,) -> Optional[json.Json]:
        """
        Gets the life property value. The life property
        Returns: Optional[json.Json]
        """
        return self._life
    
    @life.setter
    def life(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the life property value. The life property
        Args:
            value: Value to set for the life property.
        """
        self._life = value
    
    @property
    def per(self,) -> Optional[json.Json]:
        """
        Gets the per property value. The per property
        Returns: Optional[json.Json]
        """
        return self._per
    
    @per.setter
    def per(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the per property value. The per property
        Args:
            value: Value to set for the per property.
        """
        self._per = value
    
    @property
    def salvage(self,) -> Optional[json.Json]:
        """
        Gets the salvage property value. The salvage property
        Returns: Optional[json.Json]
        """
        return self._salvage
    
    @salvage.setter
    def salvage(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the salvage property value. The salvage property
        Args:
            value: Value to set for the salvage property.
        """
        self._salvage = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("cost", self.cost)
        writer.write_object_value("life", self.life)
        writer.write_object_value("per", self.per)
        writer.write_object_value("salvage", self.salvage)
        writer.write_additional_data_value(self.additional_data)
    

