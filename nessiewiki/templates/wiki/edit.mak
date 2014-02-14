<%inherit file="local:templates.master"/>

<%def name="title()">
  Editing ${page.title}
</%def>

  <div>
    <form action="/save" method="post">
      <div>
        <label for="pagetitle">Editing</label>
        <input type="text" id="pagetitle" name="pagetitle" value="${page.title}"/>
      </div>
      <textarea rows="30" cols="60" name="text">${page.text}</textarea>
      <input type="hidden" name="_id" value="${page._id}"/>
      <button type="submit">Save Page</button>
    </form>
  </div>
