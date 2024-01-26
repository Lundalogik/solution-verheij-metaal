import datetime
import logging

import limepkg_base_solution_helpers.common as base_common
import limepkg_base_solution_helpers.limeobject_classes.general as base_general
import limepkg_basic_deal.decorators as deal_decorators
from lime_type import LimeObject
from lime_type.unit_of_work import UnitOfWork

logger = logging.getLogger(__name__)


@deal_decorators.deal()
class Deal(LimeObject):
    def before_update(self, uow: UnitOfWork, **kwargs):
        super().before_update(uow, **kwargs)

        if base_general.option_changed(self, "dealstatus", to_key=["agreement"]):
            self.properties.expecteddate.value = datetime.datetime.now()

        base_common.add_history_if_option_change(
            limeobject=self,
            option_prop="dealstatus",
            uow=uow,
        )

    def before_delete(self, uow, **kwargs):
        super().before_delete(uow, **kwargs)

    def after_update(self, unsaved_self, **kwargs):
        super().after_update(unsaved_self, **kwargs)


def register_limeobject_classes(register_class):
    register_class("deal", Deal)
