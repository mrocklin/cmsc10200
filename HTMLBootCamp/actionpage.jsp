<%

 String lastnameStr = request.getParameter("lastname");
 String firstnameStr = request.getParameter("firstname");

%>

<HTML>
  <HEAD>
  </HEAD>
 <BODY>
   <P> Hello <%=firstnameStr+" "+lastnameStr%></P>
 </BODY>
</HTML>
