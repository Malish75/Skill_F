<div>
{% for val in post.category.all %}
Текущая категория - "{{val}}"
{% endfor %}
</div>

{% for val in post.category.all %}
  {% if val in user.category_set.all %}
     <button> <a href="subscribers/{{val.id}}"> Подписаться</a> </button>
  {% else %}
     <button> <a href="unsubscribers/{{val.id}}"> Отписаться</a> </button>
  {%endif%}
{% endfor %}