<!DOCTYPE html>
<html class="colour-scheme adaptive">

<head>
    <link rel="stylesheet" href="scripts/index.css">
    <link rel="stylesheet" href="scripts/navbar.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Varela Round">
    <title>Wonderfully Useless Welcome Page</title>
</head>

<body>
    <span id="header" class="center">
        <h1>Usefully Useless Things</h1>
    </span>
    <span class="navbar-container center" id="navbar">
        <?php include ("includes/navbar.php"); ?>
    </span>
    <div class="body">
        <div style="padding-left:16px">
            <h2>Welcome!</h2>
            <p>
                The purpose of this website is twofold. The primary goal is to practice my data illustration skills and
                build my toolkit as a data scientist, but also to have a collection of graphs, or charts, or anything
                that may be useful to someone; even if it may not be useful to me.
            </p>
            <p>
                To get started, click on playground and explore the world of beautifully useless things!
            </p>
            <p>
                The main initial goal of this website is to be a place to share data from the extension sites from the
                state universities around the country. Next, it will be expanded to native plant guides (preferably by
                county) which will give examples of native plants, their benefits, and the best place to buy these
                plants. These shops will be personally vetted but don't forget to always do your own research when
                buying things online!
            </p>
        </div>
        <div style="padding-left:16px">
            <h2>Things to currently do:</h2>
            <p>
                Currently the main feature of the website is the playground. It is an svg file from a forgotten author;
                with all of the state svg files coming from the wikicommons. The eventual goal is to make each state
                clickable (only a handful currently are) and then within each state there will be a populated table
                (with pictures) of native plants and vegetable planting schedules for the state/county.
            </p>
            <p>
                So, go forth and adventure around this Usefully Useless arena!
            </p>
        </div>
        <div style="padding-left:16px">
            <h2>The Future</h2>
            <p>
                There currently aren't any concrete plans for the future of this website! There are ideas and hopes and
                dreams that may come along but that will come after the first working prototype. The hope is to build a
                community where people will be able to log in to update maps and add things that they see as neat as
                well as hosting of a discussion board for projects that might be interesting to include as this site is
                being built!
            </p>
        </div>
    </div>
    <div class="centre">
        <img style="width: 21vw" alt="Flag of the Bahamas" src="index_page_flags/Flag_of_the_Bahamas.svg.png">
        <img style="width: 16vw" alt="Flag of Maryland" src="index_page_flags/Flag_of_Maryland.svg.png">
        <img style="width: 16vw" alt="Flag of Barbados" src="index_page_flags/Flag_of_Barbados.svg.png">
        <img style="width: 16vw" alt="Flag of the Czech Republic"
            src="index_page_flags/Flag_of_the_Czech_Republic.svg.png">
        <img style="width: 21vw" alt="Flag of the United States (DoS ECA Color Standard)"
            src="index_page_flags/Flag_of_the_United_States_(DoS_ECA_Color_Standard).svg.png">
    </div>

    <script type="text/javascript" src="scripts/navbar.js"></script>

</body>

</html>
