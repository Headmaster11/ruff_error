class CustomRichTextBlock():
    def get_api_representation(self, value, context=None):
        result = super().get_api_representation(value, context)
        if result.get("value"):
            result["value"] = result["value"].replace("<nbsp> </nbsp>", "&nbsp;")
        if result.get("value"):
            while True:
                nbsp_start = result["value"].find("<nbsp>")
                if nbsp_start == -1:
                    break
                nbsp_end = result["value"].find("</nbsp>")
                element = result["value"][nbsp_start + 6 : nbsp_end]
                new_end = nbsp_end + 1 if result["value"][nbsp_end + 7 ] else nbsp_end
                result["value"] = (
                    result["value"][:nbsp_start]
                    + f"{element}&nbsp;"
                    + result["value"][new_end + 7 : ]
                )

        if result.get("value"):
            result["value"] = result["value"].replace("&amp;nbsp;", "&nbsp;")
            result["value"] = result["value"].replace("&nbsp; ", "&nbsp;")
        return result
