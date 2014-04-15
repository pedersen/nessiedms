<%inherit file="local:templates.master"/>
<%!
   from tg import lurl
%>
<%def name="title()">
  ${pagetitle}
</%def>

  <div>
    <h1><em>${pagetitle}</em></h1>
  </div>
  <div>
    ${content | n}
    <a href="${lurl('%s/edit' % pagetitle)}">Edit This Page</a>
    <a href="${lurl('%s/delete' % pagetitle)}">Delete This Page</a>
  </div>
  <div>
    <p>See A List of <a href="/pagelist">All Pages</a></p>
  </div>
  
