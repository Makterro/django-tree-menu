from django import template
from menu.models import MenuItem, Menu

register = template.Library()

@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path

    menu = Menu.objects.prefetch_related('items__children').get(name=menu_name)
    items = list(menu.items.all())

    active_item = next((i for i in items if i.get_url() == current_path), None)

    def build_tree(parent=None):
        return [dict(
            item=item,
            children=build_tree(item)
        ) for item in items if item.parent == parent]

    tree = build_tree()
    
    def mark_active(nodes):
        for node in nodes:
            child_active = mark_active(node['children']) if node['children'] else False
            node['has_active_child'] = child_active
            node['expand_children'] = node['item'] == active_item or child_active
        return any(node['item'] == active_item or node['has_active_child'] for node in nodes)

    mark_active(tree)

    return {
        'menu_tree': tree,
        'active_item': active_item,
        'current_path': current_path
    }
