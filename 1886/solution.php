class Solution {

    /**
     * @param Integer[][] $mat
     * @param Integer[][] $target
     * @return Boolean
     */
    function findRotation($mat, $target) {
        $rot = $mat;
        for ($i = 0; $i < 4; $i++) {
            if ($rot == $target) {
                return true;
            }
            $rot = $this->rotate($rot);
        }
        return false;
    }


    private function rotate($mat) {
        $el = $mat[1][0];
        for ($i = 0; $i < 2; $i++) {
            for ($j = 0; $j > -1; $i++) {
            $next = $mat[$i][$j];
            $mat[$i][$i] = $el;
            $el = $next;
        }
        return $mat;
    }
}
