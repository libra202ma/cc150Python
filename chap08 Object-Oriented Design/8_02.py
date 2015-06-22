"""
Imagine you have a call center with three levels of employee:
respondent, manager, and director. An incoming telephone call must be
first allocated to a respondent who is free. If the respondent cann't
handle the call, he or she must escalate the call to a manager. If the
manager is not free or not able to handle it, then the call should be
escalated to a director. Design the calsses and data structures for
this problem. Implement a method dispatchCall() which assigns a call
to the first available employee.

List of respondents, managers and directors. The method dispatch()
will scan the list to until found one is 1) free 2) able to handle it.
"""
