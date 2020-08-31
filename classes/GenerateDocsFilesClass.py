from docxtpl import DocxTemplate

class GenerateDocsFile:

    def __init__(self, df):
        self.df = df

    def __create_file(self, row, name,template_file,output_folder):
        tpl = DocxTemplate(template_file)
        tpl.render(row)
        tpl.save(output_folder+"//%s.docx" % str(name))

    def generate_files(self,template_file,output_folder):

        for i in range(0, len(self.df)):
            row = dict(self.df.iloc[i])
            self.__create_file(row, self.df.iloc[i][0],template_file,output_folder)



