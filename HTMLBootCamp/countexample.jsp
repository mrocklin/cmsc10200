<%
int limit = 5;

%>

<HTML>
  <BODY>
    <h3> A list of Cubes </h3>

    <ul>
    <%for(int count = 1; count <= limit; count++){%>
      <li> <%=count%> cubed is <%=count*count*count%> </li>
    <%}%>
    </ul>


 </BODY>
</HTML>
