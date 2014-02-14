<%inherit file="local:templates.master"/>

<%def name="title()">
  Page Listing
</%def>

<p><a href="/edit?title=New%20Page">Create a New Page</a></p>
<ul>
% for page in pages:
  <li><a href="/${page.title}">${page.title}</a></li>
% endfor
</ul>
