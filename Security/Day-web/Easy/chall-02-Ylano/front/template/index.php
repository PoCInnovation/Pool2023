<html>

<head>
    <meta charset="UTF-8">
    <title>PoC - password = PaS$Wjrigolemdr</title>
</head>

<body>
    <link href='style.css' rel='stylesheet' type='text/css'>
    <div class="navbar">
        <ul class="navbar-container">
            <li><a href="#" class="left-underline nav-button brand-logo">PoC</a></li>
            <li class="nav-item"><a href="#" class="left-underline nav-button" data-scroll>Wallet</a></li>
            <li class="nav-item"><a href="#" class="left-underline nav-button" data-scroll>Pictures</a></li>
            <li class="nav-item active"><a href="#" class="left-underline nav-button" data-scroll>Home</a></li>
        </ul>
    </div>
    <div class="parallax p1" id="section-1">
        <hgroup>
            <h1>Challenge 04 - Ylano</h1>
            <h1>Welcome to PoC Hacking Plateform</h1>
            <h2>Will you be able to hack me ?!</h2>
            <center>
                <button type="button" class="hidden" onclick="readTextFile('static/.hidden')">Hidden</button>
            </center>
        </hgroup>
    </div>
    <div class="row">
        <div class="col-3">
            <h1>1 - Scanning vulnerabilities</h1>
            <p>In response to a budget dynamic, the structures will interact with the assessable openings. Once the
                transversality of subcontracting has been evaluated, the managers decide to audit the mobility
                alternatives. To outsource the expertise of subcontracting, it is better to perform organizational
                recapitalizations.</p>
        </div>
        <div class="col-3">
            <h1>2 - Exploiting target</h1>
            <p>To integrate an online / offline dynamic, the answer is simple: audit the decisional partners. Since the
                emergence of a quantitative dynamic, suppliers will anticipate quality management. Perpendicular to the
                operational governance, we must pilot the framework issues.</p>
        </div>
        <div class="col-3">
            <h1>3 - Maintaining access</h1>
            <p>In terms of revitalizing institutional globalization, the objective is obvious:
                <!DOCTYPE HTML>to decompartmentalize risk content. In response to the multiplicity of references, the
                ambition is clear: to revalue high-yield opportunities. Once the opportunity for intervention has been
                assessed, the mobility factors must be initiated.
            </p>
        </div>
    </div>
    <?php
    if (isset($_GET['page'])) {
        $file = $_GET['page'];
        include($file);
    }
    ?>

    <body>
        <form method="get">
            <a href="index.php?page=login.php">login</a>
        </form>
        <footer>
            <div class="footer-copyright">
                <div class="container">
                    © 2022 - PoC community, All rights reserved.
                </div>
            </div>
        </footer>
    </body>

</html>