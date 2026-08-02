from src import body_parser

html_test = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f4f4;
        }
        .hidden {
            display: none;
        }
    </style>
</head>

<body>

<table width="100%" cellpadding="0" cellspacing="0" bgcolor="#f4f4f4">
<tr>
<td align="center">

<table width="600" cellpadding="20" cellspacing="0" bgcolor="#ffffff">

<tr>
<td align="center">
<img src="https://example.com/logo.png" alt="Voxel Inc." width="120">
</td>
</tr>

<tr>
<td>

<h2>Hello Nayan 👋</h2>

<p>
Thank you for signing up for our service.
We're excited to have you onboard.
</p>

<p>
Your verification code is:
</p>

<h1 style="color:#2E86DE;">483912</h1>

<p>
This code expires in <strong>10 minutes</strong>.
</p>

<p>
<a href="https://example.com/verify?id=12345&utm_source=email">
Verify your account
</a>
</p>

<hr>

<h3>What's new?</h3>

<ul>
<li>Unlimited AI summaries</li>
<li>Priority inbox</li>
<li>Weekly digest</li>
</ul>

</td>
</tr>

<tr>
<td>

<img
    src="https://tracking.example.com/open?id=abcdef123456"
    width="1"
    height="1"
    alt=""
>

<div class="hidden">
This text is only for preview in some email clients.
</div>

</td>
</tr>

<tr>
<td style="font-size:12px;color:gray;">

You received this email because you created an account.

<br><br>

<a href="https://example.com/unsubscribe">
Unsubscribe
</a>

</td>
</tr>

</table>

</td>
</tr>
</table>

</body>
</html>
"""

print(body_parser.parse_html(html_test))