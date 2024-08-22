import json
import os
from itemadapter import ItemAdapter

class JsonWriterPipeline:
    def open_spider(self, spider):
        file_path = os.path.join("./output", f'{spider.run_id}.jsonl')
        self.file = open(file_path, "a")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item