from loader import dp
from filters.admins import AdminFilter
from filters.group_filter import IsGroup
from filters.private_chat import IsPrivate


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)
