from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class WindowsInformationProtectionDataRecoveryCertificate(AdditionalDataHolder, BackedModel, Parsable):
    """
    Windows Information Protection DataRecoveryCertificate
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Data recovery Certificate
    certificate: Optional[bytes] = None
    # Data recovery Certificate description
    description: Optional[str] = None
    # Data recovery Certificate expiration datetime
    expiration_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Data recovery Certificate subject name
    subject_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsInformationProtectionDataRecoveryCertificate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsInformationProtectionDataRecoveryCertificate
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WindowsInformationProtectionDataRecoveryCertificate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "certificate": lambda n : setattr(self, 'certificate', n.get_bytes_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "subjectName": lambda n : setattr(self, 'subject_name', n.get_str_value()),
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
        writer.write_bytes_value("certificate", self.certificate)
        writer.write_str_value("description", self.description)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("subjectName", self.subject_name)
        writer.write_additional_data_value(self.additional_data)
    

