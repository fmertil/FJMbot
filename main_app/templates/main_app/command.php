<?php
    $last = exec('ls', $o, $r);
    if ($r != 0)
    {
        print 'Error running command';
        exit($r);
    }
    else
        print implode("\n", $o);
?>
