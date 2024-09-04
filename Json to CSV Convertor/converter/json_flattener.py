class JSONFlattener:
    def flatten(self, obj):
        flattened = {}
        for key, value in obj.items():
            if isinstance(value, dict):
                flattened.update(self.flatten(value))
            elif isinstance(value, list):
                for item in value:
                    flattened[f"{key}.{item}"] = item
            else:
                flattened[key] = value
        return flattened
