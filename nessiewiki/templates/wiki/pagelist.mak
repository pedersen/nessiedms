<%inherit file="local:templates.master"/>

<%def name="title()">
  Page Listing
</%def>

<ul>
% for page in pages:
  <li><a href="/${page.title}">${page.title}</a></li>
% endfor
</ul>
