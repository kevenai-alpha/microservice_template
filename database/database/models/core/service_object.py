from sqlalchemy import Column, func, Text, DateTime, text
from sqlalchemy.dialects.postgresql import UUID, JSONB


class ServiceObject(object):
    # Setting primary_key=True includes nullable=False
    id = Column(
        UUID, primary_key=True, server_default=text("uuid_generate_v4()")
    )

    # NOTE: clock_timestamp() is non standard SQL.
    #       current_timestamp() is standard, but only returns
    #       the timestamp at the start of a transaction
    date_created = Column(
        DateTime(timezone=True), server_default=func.clock_timestamp()
    )
    last_updated = Column(
        DateTime(timezone=True),
        server_default=func.clock_timestamp(),
        onupdate=func.clock_timestamp(),
    )
    data_origin = Column(Text, nullable=True)

    meta_data = Column(JSONB, nullable=True)


