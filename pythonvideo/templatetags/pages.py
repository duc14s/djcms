from django import template
 
register = template.Library()
 
@register.simple_tag
def current_page(page):
        html=""
        for i in range(1,11):
            if page == i:
                html += '<li class="active"> <span class="sr-only">%d</span></li>' % i
            else:
                html +='<li><a href="/videos?page=%d" >%d</a></li>'%(i,i)
         
        return html
