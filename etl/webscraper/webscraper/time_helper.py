import datetime

class TimeHelper():
    def get_utc_now(self):
        return datetime.datetime.now(datetime.timezone.utc)

    def get_elapsed_seconds(self, start_time: datetime):
        return (self.get_utc_now() - start_time).total_seconds()