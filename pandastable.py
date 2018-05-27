from pandas import DataFrame
import types


class PandasTable(DataFrame):
    """
    We can have dt('a==1')
    Then operations on that dt('a==1',sum(species)')
    """

    def __call__(self, *args, **kwargs):

        return (self._querycheck(args)._groupcheck(args,
                                                   kwargs)._colcheck(args))

    def _groupcheck(self, args, kwargs):
        """If there is a groupby operation in the arguments, apply it"""

        print(kwargs)
        if "by" in kwargs:
            if self._getfunc(args):
                return PandasTable(
                    self.groupby(kwargs["by"]).apply(self._getfunc(args)))
            else:
                raise Exception("No function was defined")
        return self

    def _querycheck(self, args):
        """
        If there is a query in the arguments, use it. In any case, return the
        dataframe
        """

        for arg in args:
            if type(arg) == str and arg != 'N':
                return PandasTable(self.query(arg))
        return self

    def _colcheck(self, args):
        """
        If there is a column subsetting operation, do it
        """

        for arg in args:
            if type(arg) == list:
                return PandasTable(self.loc[:, arg])
        return self

    def _getfunc(self, args):
        """
        Returns a function, if present in the arguments
        """
        for arg in args:

            if isinstance(arg, types.FunctionType) or isinstance(
                    arg, types.BuiltinMethodType) or isinstance(
                        arg, types.BuiltinFunctionType):
                return arg
            if arg == 'N':
                return len
        return None


_N = "N"
