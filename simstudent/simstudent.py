"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment

class simstudentXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """
    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.
    # TO-DO: change the default href so it is included as a resource in the xblock, not an url
    href = String(display_name="href",
                  default="http://kona.education.tamu.edu:2401/SimStudentServlet%20%28Working%29/tutor.html?BRD=http%3A%2F%2Fkona.education.tamu.edu%3A2401%2FSimStudentServlet%2Fif_p_or_q_then_r.brd&ARG=-traceOn+-folder+informallogic+-problem+if_p_or_q_then_r+-ssTypeChecker+informallogic.MyFeaturePredicate.valueTypeChecker&CSS=&INFO=&BRMODE=AuthorTimeTutoring&AUTORUN=on&KEYBOARDGROUP=Disabled&BACKDIR=http%3A%2F%2Fkona.education.tamu.edu%3A2401%2FSimStudentServlet%2Fbuild%2Fclasses&BACKENTRY=interaction.ModelTracerBackend&PROBLEM=xxx&DATASET=FlashLoggingTest_xxx&LEVEL1=Unit1&TYPE1=unit&USER=qa-test&GENERATED=on&SOURCE=PACT_CTAT_HTML5&USEOLI=false&SLOG=true&LOGTYPE=None&DISKDIR=.&PORT=4000&REMOTEURL=serv&SKILLS=&VAR1=xxx_xxx&VAL1=xxx&VAR2=xxx_xxx&VAL2=xxx&VAR3=xxx_xxx&VAL3=xxx&VAR4=xxx_xxx&VAL4=xxx&submit=Launch+HTML5+Tutor",
                  scope=Scope.content,
                  help="Simstudent file that will be shown in the XBlock")

    display_name = String(display_name="Display Name",
                          default="Simstudent File",
                          scope=Scope.settings,
                          help="Name of the component in the edxplatform")
    name = String(display_name="name",
                    default="if_p_or_q_then_r.brd",
                    scope=Scope.content,
                    help="Name of the brd file to run")
    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")


    def student_view(self, context=None):
        """
        The primary view of the simstudentXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/simstudent.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/simstudent.css"))
        return frag


    def studio_view(self, context=None):
        """
        The primary view of the simstudentXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/simstudent_edit.html")
        frag = Fragment(html.format(self=self))
        frag.add_javascript(self.resource_string("static/js/src/simstudent_edit.js"))
        frag.initialize_js('simstudentXBlock')
        return frag

    @XBlock.json_handler
    def save_simstudent(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        self.href = data['href']
        self.display_name = data['display_name']

        return {'result': 'success'}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("simstudentXBlock",
             """<vertical_demo>
                <simstudent/>
                </vertical_demo>
             """),
        ]
