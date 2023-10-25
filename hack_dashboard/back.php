<?php
    include("includes/db.inc.php");

    $id = $_GET["ID"];
    
    $sql = "SELECT * FROM wine WHERE id =" . $id;
    $result = mysqli_query($conn, $sql);

    $row=mysqli_fetch_assoc($result);
?>


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="style.css">
    <title>Index</title>
</head>

<body>
    <main>
        <div class="flex w-screen h-screen wp-0 m-0">
		<div class="flex w-3/4 h-3/4 m-auto border-secondary fourth">
			<div class="m-auto ms-8 w-1/4">
                    <img class="rounded"
                        src="<?= $row["path"] ?>" alt=""
                        width="400em" />
                </div>
                <div class="flex w-3/4">
                    <div class="w-3/4 h-auto m-auto">
                        <div class="m-auto flex w-full">
                            <p class="my-auto me-6 text-lg">Name:</p>
                            <p class="my-auto border-b-2 border-stone-800 my-8 text-lg w-3/4">
                                <?= $row["name"] ?>
                            </p>
                        </div>
                        <div class="m-auto flex w-full">
                            <p class="my-auto me-6 text-lg">Price:</p>
                            <p class="my-auto border-b-2 border-stone-800 my-8 text-lg w-3/4">
                                <?= $row["price"]?>€
                            </p>
                        </div>
                        <div class="m-auto flex w-full">
                            <p class="my-auto me-6 text-lg">Location:</p>
                            <p class="my-auto border-b-2 border-stone-800 my-8 text-lg w-3/4">
                                <?= $row["store"] ?>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>
</body>

</html>l