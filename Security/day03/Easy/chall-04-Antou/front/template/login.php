<html>
    <head>
        <meta charset="UTF-8">
        <title>PoC - Antou</title>
    </head>
    <body>
        <link href='static/style.css' rel='stylesheet' type='text/css'>
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
                <h1>Challenge 04 - Antou</h1>
                <h1>Welcome to PoC Hacking Plateform</h1>
                <h2>Will you be able to hack me ?!</h2>
                <form method="GET">
                    <!-- <textarea name="username" placeholder="UserName"></textarea> -->
                    <input name="username" placeholder="UserName"><br>
                    <input type="password" name="password" placeholder="Password"><br>
                    <button type="submit">Login</button>
                </form>
                <h2>Login result</h2>
                <?php
                    $input = $argv[1];
                    $flag = $argv[2];
                    echo nl2br ("<h3 style='color:black'>$input sadly isn't a valid credential :(</h3>");
                    if (strstr($input, "\n")) {
                        echo nl2br("<h2 style='color:black'> flag = THE_PASSPHRASE</h2>");
                    }
                ?>
            </hgroup>
        </div>
        <div class="row">
            <div class="col-3">
                <h1>1 - Scanning vulnerabilities</h1>
                <p>In response to a budget dynamic, the structures will interact with the assessable openings. Once the transversality of subcontracting has been evaluated, the managers decide to audit the mobility alternatives. To outsource the expertise of subcontracting, it is better to perform organizational recapitalizations.</p>
            </div>
            <div class="col-3">
                <h1>2 - Exploiting target</h1>
                <p>To integrate an online / offline dynamic, the answer is simple: audit the decisional partners. Since the emergence of a quantitative dynamic, suppliers will anticipate quality management. Perpendicular to the operational governance, we must pilot the framework issues.</p>
            </div>
            <div class="col-3">
                <h1>3 - Maintaining access</h1>
                <p>In terms of revitalizing institutional globalization, the objective is obvious: <!DOCTYPE HTML>to decompartmentalize risk content. In response to the multiplicity of references, the ambition is clear: to revalue high-yield opportunities. Once the opportunity for intervention has been assessed, the mobility factors must be initiated.</p>
            </div>
        </div>
        <footer>
            <div class="footer-copyright">
                <div class="container">
                    © 2022 - PoC community, All rights reserved.
                </div>
            </div>
        </footer>
    </body>
</html>