<%
  //Java Code
  String limitString = request.getParameter("limit");

  int limit = Integer.parseInt(limitString);

%>

<HTML>
  <BODY>
    <h3> A list of Cubes </h3>

    <ul>
    <%for(int count = 1; count <= limit; count++){%>
      <li> <%=count%> cubed is <%=count*count*count%> </li>
    <%}%>


 </BODY>
</HTML>
