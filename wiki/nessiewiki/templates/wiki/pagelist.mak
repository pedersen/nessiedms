<%inherit file="local:templates.master"/>
<%!
   from tg import lurl
%>
<%def name="title()">
  Page Listing
</%def>

<p><form action="${url('/newpage')}">Create a New Page named: <input type="text" name="title" value="New Page"/><button type="Submit">Go!</button></p>
<ul>
% for page in pages:
  <li><a href="/${page.title}">${page.title}</a></li>
% endfor
</ul>

