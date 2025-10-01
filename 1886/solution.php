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
        // do nothing, placeholder like Python pass
        return $mat;
    }
}
