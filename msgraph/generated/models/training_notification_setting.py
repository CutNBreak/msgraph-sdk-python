from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_end_user_notification import BaseEndUserNotification
    from .end_user_notification_setting import EndUserNotificationSetting
    from .training_reminder_notification import TrainingReminderNotification

from .end_user_notification_setting import EndUserNotificationSetting

@dataclass
class TrainingNotificationSetting(EndUserNotificationSetting):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.trainingNotificationSetting"
    # Training assignment details.
    training_assignment: Optional[BaseEndUserNotification] = None
    # Training reminder details.
    training_reminder: Optional[TrainingReminderNotification] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TrainingNotificationSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TrainingNotificationSetting
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TrainingNotificationSetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .base_end_user_notification import BaseEndUserNotification
        from .end_user_notification_setting import EndUserNotificationSetting
        from .training_reminder_notification import TrainingReminderNotification

        from .base_end_user_notification import BaseEndUserNotification
        from .end_user_notification_setting import EndUserNotificationSetting
        from .training_reminder_notification import TrainingReminderNotification

        fields: Dict[str, Callable[[Any], None]] = {
            "trainingAssignment": lambda n : setattr(self, 'training_assignment', n.get_object_value(BaseEndUserNotification)),
            "trainingReminder": lambda n : setattr(self, 'training_reminder', n.get_object_value(TrainingReminderNotification)),
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
        writer.write_object_value("trainingAssignment", self.training_assignment)
        writer.write_object_value("trainingReminder", self.training_reminder)
    

