<html xmlns:py="http://purl.org/kid/ns#" >
  <head>
    <title py:content="title"></title>
    ${include_css()}
    <script type="text/javascript" src="js/jquery-1.3.2.min.js"></script>
    <script type="text/javascript" src="js/common.js"></script>
  </head>
  <body>

    <div id="wrapper">
    	 <div id="header">
		<h1>${sitename}</h1>
		<div id="search">
			<form method="get" action="/search">
				<p><input type="text" name="search" />
				<input type="submit" value="${search}" /></p>
			</form>
		</div>
	 </div>
	 <div id="navigation">
	   <ul>
	     <li><a href="/">${startpage}</a></li>
	     <li><a href="/projects">${project}</a></li>
	     <li><a href="/techniques">${techniques}</a></li>
	   </ul>
	 </div>
	 <div id="container">
		<content></content>

		<div id="sidebar">
		<h3>${latest_projects}</h3>
		<ul py:for="project in latest_projects_data">
			<li><a href="/projects?id=${project['project_no']}">${project['project_name']}</a></li>
		</ul>
		</div>
	 </div>
	 <div id="footer">
	   &copy; 2009 <a href="http://www.zencodez.net/">Han Lin Yap</a> &amp; Alexander Östman
	 </div>

    </div>

  </body>
</html>
