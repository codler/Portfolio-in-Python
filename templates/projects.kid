<html py:layout="'common.kid'" xmlns:py="http://purl.org/kid/ns#">

  <link py:def="include_css()"
    href="style/layout.css" type="text/css" rel="stylesheet" />

  <div py:match="item.tag == 'content'" id="content">
    <h1>${headline}</h1>
	<p>${project_not_found}</p>
	<p py:for="project in projects">
	<a href="/projects?id=${project['project_no']}" >
		<img py:if="project['small_image'] != None" src="${project['small_image']}" />
		<img py:if="project['small_image'] == None" src="images/projects_default_small.png" />
		${project['project_name']}
	</a>
	</p>
	<p></p>
  </div>
</html>
