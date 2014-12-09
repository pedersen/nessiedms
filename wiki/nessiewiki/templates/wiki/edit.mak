<%inherit file="local:templates.master"/>
<%!
   from tg import lurl
%>
<%def name="title()">
  Editing ${page.title}
</%def>

  <div>
    <form action="${lurl('./save')}" method="post">
      <div>
        <p>${page.title}</p>
      </div>
      <textarea rows="30" cols="60" name="text">${page.text}</textarea>
      <button type="submit">Save Page</button>
    </form>
  </div>
