<html py:layout="'common.kid'" xmlns:py="http://purl.org/kid/ns#">

  <link py:def="include_css()"
    href="style/layout.css" type="text/css" rel="stylesheet" />

  <div py:match="item.tag == 'content'" id="content">
    <h1>${headline}</h1>
	<p>${project_not_found}</p>
	<p py:for="technique in techs">
	<span><b>${technique['name']} - ${technique['count']}</b></span><br />
	<span py:for="project in technique['projects']">
		<a href="/projects?id=${project['id']}" py:content="project['name']"></a>
	</span><br /><br />
	</p>
	<p></p>
  </div>
</html>
