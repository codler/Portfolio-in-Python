<html py:layout="'common.kid'" xmlns:py="http://purl.org/kid/ns#">

  <link py:def="include_css()"
    href="style/layout.css" type="text/css" rel="stylesheet" />

  <div py:match="item.tag == 'content'" id="content">
    <h1>${headline}</h1>
	<p>
		<img py:if="big_image != None" src="${big_image}" />
		<img py:if="big_image == None" src="images/projects_default_big.png" />
	</p>
	<p>Projektet startades: ${start_date} slutfördes: ${end_date}</p>
	<p>Kurs: ${course_id} - ${course_name}, ${academic_credits} hp</p>
	<p>Gruppstorlek: ${group_size}</p>
	<p>Tekniker: ${techniques_used}</p>
	<p>Externa länkar: <a href="${external_link}">${external_link}</a></p>
	<p></p>
	<p>Beskrivning: <br />${long_description}</p>
  </div>
</html>
