<html py:layout="'common.kid'" xmlns:py="http://purl.org/kid/ns#">

  <link py:def="include_css()"
    href="style/layout.css" type="text/css" rel="stylesheet" />

  <div py:match="item.tag == 'content'" id="content">
    <h1>${headline}</h1>
	<p>${project_not_found}</p>
	<p>
	<form id="advanced_search" method="get" action="/search">
		<label>${search_word}</label><input type="text" name="search" class="advanced-search"/>
		<input type="submit" value="${search}" />
		<br />
		<label>${sort_by}</label>
		<select name="sort_by">
			<option value="start_date" selected="selected">${standard}</option>
			<option py:for="field in search_fields" py:if="field != 'techniques_used' and field != 'small_image' and field != 'big_image' and field != 'long_description' and field != 'short_description' and field != 'external_link'"  py:content="translate_field[field]" value="${field}" ></option>
		</select>
		<select name="sort_order">
			<option value="asc">${ascending}</option>
			<option value="desc">${descending}</option>
		</select>
		<br />
		<label>${search_by_field}</label>
		<select name="search_fields" id="search_field" multiple="multiple" size="5">
			<option value="" selected="selected">${all}</option>
			<option py:for="field in search_fields" py:if="field != 'techniques_used' and field != 'small_image' and field != 'big_image'" py:content="translate_field[field]" value="${field}" ></option>
		</select>
		
		<label>${techniques}</label>
		<select name="techniques" multiple="multiple" size="5">
			<option value="" selected="selected">${all}</option>
			<option py:for="technique in techs" value="${technique}">${technique}</option>
		</select>
	</form>
	</p>
	<hr />
	<p py:if="results == []">${projects_not_found}</p>
	<p py:for="result in results">
	<a href="/projects?id=${result['project_no']}">		
		<img py:if="result['small_image'] != None" src="${result['small_image']}" />
		<img py:if="result['small_image'] == None" src="images/projects_default_small.png" />
		${result['project_name']}
	</a>
	</p>
	<p></p>
  </div>
</html>
