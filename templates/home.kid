<html py:layout="'common.kid'" xmlns:py="http://purl.org/kid/ns#">

  <link py:def="include_css()"
    href="style/layout.css" type="text/css" rel="stylesheet" />

  <div py:match="item.tag == 'content'" id="content">
    <h1>${headline}</h1>
	<p>Personligt projekt portfolio för Han Lin Yap &amp; Alexander Östman.</p>
	<p></p>
  </div>
</html>
