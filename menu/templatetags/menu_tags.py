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
        nodes = []
        for item in items:
            if item.parent == parent:
                children = build_tree(item)
                has_active_child = any(c['expand_children'] for c in children)
                expand_children = item == active_item or has_active_child
                nodes.append({
                    'item': item,
                    'children': children,
                    'has_active_child': has_active_child,
                    'expand_children': expand_children
                })
        return nodes

    tree = build_tree()

    return {
        'menu_tree': tree,
        'active_item': active_item,
        'current_path': current_path
    }
