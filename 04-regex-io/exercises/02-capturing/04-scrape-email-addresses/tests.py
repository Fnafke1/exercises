@pytest.mark.parametrize("string", [
        'a@c.com',
        '111@AFF.com',
        '*a@b*',
        """
        a@c.com fsjdf jfslk fkls fjl df
        jalfkj b@d.be fjdlkf jfkljdlkf
        qpoiopc fdfqpof ifppopo fkpqo
        qfjlkl xyz@ppp.fr jkfljqlkj
        opfpqsjkl<...@...>
        """,
])
def test_function(string):
    function_name = 'scrape_email_addresses'
    assert hasattr(student, function_name), f"Missing function {function_name}"

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(string)
    expected = solution_function(string)

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"