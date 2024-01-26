import logging

import limepkg_base_solution_helpers.common as base_common
import limepkg_basic_lead.decorators as lead_decorators
from lime_type import LimeObject
from lime_type.unit_of_work import UnitOfWork

logger = logging.getLogger(__name__)


@lead_decorators.lead()
class Lead(LimeObject):
    def before_update(self, uow: UnitOfWork, **kwargs):
        super().before_update(uow, **kwargs)

        base_common.add_history_if_option_change(
            limeobject=self,
            option_prop="leadstatus",
            uow=uow,
        )

    def before_delete(self, uow, **kwargs):
        super().before_delete(uow, **kwargs)

    def after_update(self, unsaved_self, **kwargs):
        super().after_update(unsaved_self, **kwargs)


def register_limeobject_classes(register_class):
    register_class("lead", Lead)
