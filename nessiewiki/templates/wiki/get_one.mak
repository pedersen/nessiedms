<%inherit file="local:templates.master"/>

<%def name="title()">
  ${pagetitle}
</%def>

  <div>
    <h1>Viewing <em>${pagetitle}</em></h1>
  </div>
  <div>
    ${content | n}
    <a href="/edit?_id=${_id}">Edit This Page</a>
  </div>
  <div>
    <p>See A List of <a href="/pagelist">All Pages</a></p>
  </div>
  
