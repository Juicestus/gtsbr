function toggle() 
{
    var button = document.getElementById('toggle').innerHTML;
    var style = "";
    var pstyle = "";
    var toggle = "";
    if (button == "Dark Mode") 
    {
        toggle = "Light Mode";
        style = dark;
        pstyle = pdark;
    }
    else if (button == "Light Mode") 
    {
        toggle = "Dark Mode";
        style = light;
        pstyle = plight;
    }
    document.getElementById('toggle').innerHTML = toggle;
    document.getElementById('style').innerHTML = style;
    document.getElementById('pstyle').innerHTML = pstyle;
}