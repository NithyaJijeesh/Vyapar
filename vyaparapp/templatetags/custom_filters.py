from django import template

register = template.Library()

@register.filter
def last_item_for_bill(history_list, bill):
    filtered_list = [item for item in history_list if item.purchasebill == bill]
    if filtered_list:
        return filtered_list[-1].action, filtered_list[-1].staff.first_name + " " + filtered_list[-1].staff.last_name
    return None
