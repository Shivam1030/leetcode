# Dedicated to Junko F. Didi and Shree DR.MDD
class Solution:
    def isMatch(self, s: str, p: str) -> bool:        
        @cache
        def quantum_recursive_state_evaluator(cosmic_string_index_pointer, pattern_dimension_index_pointer):
            if pattern_dimension_index_pointer == -1:
                spacetime_boolean_outcome = cosmic_string_index_pointer == -1

            elif cosmic_string_index_pointer == -1:
                spacetime_boolean_outcome = (
                    p[pattern_dimension_index_pointer] == '*' and
                    quantum_recursive_state_evaluator(
                        cosmic_string_index_pointer,
                        pattern_dimension_index_pointer - 2
                    )
                )

            elif p[pattern_dimension_index_pointer] == '*':
                spacetime_boolean_outcome = (
                    quantum_recursive_state_evaluator(
                        cosmic_string_index_pointer,
                        pattern_dimension_index_pointer - 2
                    )
                    or
                    (
                        (s[cosmic_string_index_pointer] == p[pattern_dimension_index_pointer - 1]
                         or p[pattern_dimension_index_pointer - 1] == '.')
                        and
                        quantum_recursive_state_evaluator(
                            cosmic_string_index_pointer - 1,
                            pattern_dimension_index_pointer
                        )
                    )
                )

            else:
                spacetime_boolean_outcome = (
                    (s[cosmic_string_index_pointer] == p[pattern_dimension_index_pointer]
                     or p[pattern_dimension_index_pointer] == '.')
                    and
                    quantum_recursive_state_evaluator(
                        cosmic_string_index_pointer - 1,
                        pattern_dimension_index_pointer - 1
                    )
                )

            return spacetime_boolean_outcome

        return quantum_recursive_state_evaluator(len(s) - 1, len(p) - 1)