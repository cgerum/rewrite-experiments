"""Definition of meta model 'model'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from pyecore.ecore import EIntegerObject, EString, ELong, EInt, EBoolean, EBigInteger, EDouble, EDoubleObject, EFloat, ELongObject


name = 'model'
nsURI = 'http://app4mc.eclipse.org/amalthea/2.2.0'
nsPrefix = 'am'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
RelationalOperator = EEnum('RelationalOperator', literals=[
                           '_undefined_', 'EQUAL', 'NOT_EQUAL', 'LESS_THAN', 'LESS_THAN_OR_EQUAL', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL'])

ParameterType = EEnum('ParameterType', literals=[
                      '_undefined_', 'Integer', 'Float', 'Bool', 'String', 'Time'])

TimeUnit = EEnum('TimeUnit', literals=['_undefined_', 's', 'ms', 'us', 'ns', 'ps'])

FrequencyUnit = EEnum('FrequencyUnit', literals=['_undefined_', 'Hz', 'kHz', 'MHz', 'GHz'])

VoltageUnit = EEnum('VoltageUnit', literals=['_undefined_', 'uV', 'mV', 'V'])

DataSizeUnit = EEnum('DataSizeUnit', literals=['_undefined_', 'bit', 'kbit', 'Mbit', 'Gbit', 'Tbit',
                     'Kibit', 'Mibit', 'Gibit', 'Tibit', 'B', 'kB', 'MB', 'GB', 'TB', 'KiB', 'MiB', 'GiB', 'TiB'])

DataRateUnit = EEnum('DataRateUnit', literals=['_undefined_', 'bitPerSecond', 'kbitPerSecond', 'MbitPerSecond', 'GbitPerSecond', 'TbitPerSecond', 'KibitPerSecond', 'MibitPerSecond',
                     'GibitPerSecond', 'TibitPerSecond', 'BPerSecond', 'kBPerSecond', 'MBPerSecond', 'GBPerSecond', 'TBPerSecond', 'KiBPerSecond', 'MiBPerSecond', 'GiBPerSecond', 'TiBPerSecond'])

SamplingType = EEnum('SamplingType', literals=[
                     'default', 'BestCase', 'WorstCase', 'AverageCase', 'CornerCase', 'Uniform'])

InterfaceKind = EEnum('InterfaceKind', literals=[
                      '_undefined_', 'provides', 'requires', 'provides_requires'])

RunnableOrderType = EEnum('RunnableOrderType', literals=[
                          '_undefined_', 'successor', 'immediateSuccessorStartSequence', 'immediateSuccessorAnySequence', 'immediateSuccessorEndSequence'])

EventChainItemType = EEnum('EventChainItemType', literals=['_undefined_', 'sequence', 'parallel'])

SynchronizationType = EEnum('SynchronizationType', literals=['_undefined_', 'Stimulus', 'Response'])

MappingType = EEnum('MappingType', literals=[
                    '_undefined_', 'OneToOne', 'Reaction', 'UniqueReaction'])

LatencyType = EEnum('LatencyType', literals=['_undefined_', 'Age', 'Reaction'])

Severity = EEnum('Severity', literals=['_undefined_', 'Cosmetic', 'Minor', 'Major', 'Critical'])

LimitType = EEnum('LimitType', literals=['_undefined_', 'UpperLimit', 'LowerLimit'])

TimeMetric = EEnum('TimeMetric', literals=['_undefined_', 'ActivateToActivate', 'CoreExecutionTime', 'EndToEnd', 'EndToStart', 'GrossExecutionTime', 'Lateness',
                   'MemoryAccessTime', 'NetExecutionTime', 'OsOverhead', 'ParkingTime', 'PollingTime', 'ReadyTime', 'ResponseTime', 'RunningTime', 'StartDelay', 'StartToStart', 'WaitingTime'])

CountMetric = EEnum('CountMetric', literals=['_undefined_', 'Activations', 'BoundedMigrations',
                    'CacheHit', 'CacheMiss', 'FullMigrations', 'MtaLimitExceeding', 'Preemptions'])

PercentageMetric = EEnum('PercentageMetric', literals=['_undefined_', 'CacheHitRatio', 'CacheMissRatio', 'CoreExecutionTimeRelative',
                         'MemoryAccessTimeRelative', 'NormalizedLateness', 'NormalizedResponseTime', 'OsOverheadRelative'])

CPUPercentageMetric = EEnum('CPUPercentageMetric', literals=[
                            '_undefined_', 'CPUBuffering', 'CPULoad', 'CPUParking', 'CPUPolling', 'CPUReady', 'CPURunning', 'CPUWaiting'])

FrequencyMetric = EEnum('FrequencyMetric', literals=[
                        '_undefined_', 'CacheHitFrequency', 'CacheMissFrequency'])

CoherencyDirection = EEnum('CoherencyDirection', literals=['_undefined_', 'input', 'output'])

ProcessEventType = EEnum('ProcessEventType', literals=['_all_', 'activate', 'start', 'resume', 'preempt',
                         'poll', 'run', 'wait', 'poll_parking', 'park', 'release_parking', 'release', 'terminate'])

RunnableEventType = EEnum('RunnableEventType', literals=[
                          '_all_', 'start', 'suspend', 'resume', 'terminate'])

LabelEventType = EEnum('LabelEventType', literals=['_all_', 'read', 'write'])

ModeLabelEventType = EEnum('ModeLabelEventType', literals=[
                           '_all_', 'read', 'write', 'increment', 'decrement'])

ChannelEventType = EEnum('ChannelEventType', literals=['_all_', 'send', 'receive'])

SemaphoreEventType = EEnum('SemaphoreEventType', literals=['_all_', 'lock', 'unlock'])

ComponentEventType = EEnum('ComponentEventType', literals=['_all_', 'start', 'end'])

MemoryType = EEnum('MemoryType', literals=['_undefined_', 'DRAM', 'SRAM', 'FLASH', 'PCM'])

StructureType = EEnum('StructureType', literals=[
                      '_undefined_', 'System', 'ECU', 'Microcontroller', 'SoC', 'Cluster', 'Group', 'Array', 'Area', 'Region'])

CacheType = EEnum('CacheType', literals=['_undefined_', 'instruction', 'data', 'unified'])

PortType = EEnum('PortType', literals=['_undefined_', 'initiator', 'responder'])

SchedPolicy = EEnum('SchedPolicy', literals=['_undefined_', 'RoundRobin', 'FCFS', 'PriorityBased'])

WriteStrategy = EEnum('WriteStrategy', literals=[
                      '_undefined_', 'none', 'writeback', 'writethrough'])

PuType = EEnum('PuType', literals=['_undefined_', 'GPU', 'CPU', 'Accelerator'])

PortInterface = EEnum('PortInterface', literals=[
                      '_undefined_', 'custom', 'CAN', 'Flexray', 'LIN', 'MOST', 'Ethernet', 'SPI', 'I2C', 'AXI', 'AHB', 'APB', 'SWR'])

HwFeatureType = EEnum('HwFeatureType', literals=[
                      '_undefined_', 'performance', 'power', 'performance_and_power'])

MemoryAddressMappingType = EEnum('MemoryAddressMappingType', literals=[
                                 '_undefined_', 'none', 'address', 'offset'])

OsDataConsistencyMode = EEnum('OsDataConsistencyMode', literals=[
                              '_undefined_', 'noProtection', 'automaticProtection', 'customProtection', 'handledByModelElements'])

AccessMultiplicity = EEnum('AccessMultiplicity', literals=[
                           '_undefined_', 'singleAccess', 'multipleAccesses'])

DataStabilityLevel = EEnum('DataStabilityLevel', literals=[
                           '_undefined_', 'period', 'process', 'scheduleSection', 'runnable'])

SemaphoreType = EEnum('SemaphoreType', literals=[
                      '_undefined_', 'CountingSemaphore', 'Resource', 'Spinlock'])

CombinatorialCondition = EEnum('CombinatorialCondition', literals=[
                               '_undefined_', 'requires', 'excludes'])

GroupingType = EEnum('GroupingType', literals=['_undefined_', 'allOfThem', 'atLeastOneOfThem'])

CurveType = EEnum('CurveType', literals=['_undefined_', 'sine', 'triangle'])

WaitEventType = EEnum('WaitEventType', literals=['_undefined_', 'AND', 'OR'])

WaitingBehaviour = EEnum('WaitingBehaviour', literals=['_undefined_', 'active', 'passive'])

ISRCategory = EEnum('ISRCategory', literals=['_undefined_', 'CATEGORY_1', 'CATEGORY_2'])

AccessPrecedenceType = EEnum('AccessPrecedenceType', literals=[
                             '_undefined_', 'defaultWR', 'ignoreWR', 'enforceRW'])

OrderType = EEnum('OrderType', literals=['_undefined_',
                  'order', 'directOrder', 'startSequence', 'endSequence'])

DirectionType = EEnum('DirectionType', literals=['_undefined_', 'in_', 'out', 'inout'])

LabelDataStability = EEnum('LabelDataStability', literals=[
                           '_undefined_', 'noProtection', 'automaticProtection', 'customProtection', 'handledByModelElements'])

ModeLabelAccessEnum = EEnum('ModeLabelAccessEnum', literals=[
                            '_undefined_', 'read', 'set', 'increment', 'decrement'])

ReceiveOperation = EEnum('ReceiveOperation', literals=[
                         '_undefined_', 'FIFO_Read', 'FIFO_Take', 'LIFO_Read', 'LIFO_Take'])

LabelAccessDataStability = EEnum('LabelAccessDataStability', literals=[
                                 '_undefined_', 'inherited', 'noProtection', 'automaticProtection', 'customProtection', 'handledByModelElements'])

LabelAccessEnum = EEnum('LabelAccessEnum', literals=['_undefined_', 'read', 'write'])

LabelAccessImplementation = EEnum('LabelAccessImplementation', literals=[
                                  '_undefined_', 'explicit', 'implicit', 'timed'])

SemaphoreAccessEnum = EEnum('SemaphoreAccessEnum', literals=[
                            '_undefined_', 'request', 'exclusive', 'release'])

BlockingType = EEnum('BlockingType', literals=[
                     '_undefined_', 'active_wait', 'passive_wait', 'non_blocking'])

Preemption = EEnum('Preemption', literals=['_undefined_',
                   'preemptive', 'cooperative', 'non_preemptive'])

ConcurrencyType = EEnum('ConcurrencyType', literals=[
                        '_undefined_', 'SingleCoreSafe', 'MultiCoreSafe', 'SingleCorePrioSafe'])

ASILType = EEnum('ASILType', literals=['_undefined_', 'D', 'C', 'B', 'A', 'QM'])

ArithmeticOperator = EEnum('ArithmeticOperator', literals=[
                           '_undefined_', 'ADD', 'SUBTRACT', 'MULTIPLY', 'MODULO'])


Address = EDataType('Address', instanceClassName='long')

PositiveInt = EDataType('PositiveInt', instanceClassName='int')

PositiveLong = EDataType('PositiveLong', instanceClassName='long')

PositiveDouble = EDataType('PositiveDouble', instanceClassName='double')

NonNegativeInt = EDataType('NonNegativeInt', instanceClassName='int')

NonNegativeLong = EDataType('NonNegativeLong', instanceClassName='long')

NonNegativeDouble = EDataType('NonNegativeDouble', instanceClassName='double')


@abstract
class IAnnotatable(EObject, metaclass=MetaEClass):
    """IAnnotatable: Possibility to store custom properties on elements"""
    customProperties = EReference(ordered=True, unique=True,
                                  containment=True, derived=False, upper=-1)

    def __init__(self, *, customProperties=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if customProperties:
            self.customProperties.extend(customProperties)


@abstract
class ITaggable(EObject, metaclass=MetaEClass):
    """ITaggable: Possibility to add tags to an elements"""
    tags = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, tags=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if tags:
            self.tags.extend(tags)


@abstract
class INamed(EObject, metaclass=MetaEClass):
    """INamed: Name attribute"""
    name = EAttribute(eType=EString, unique=False, derived=False, changeable=True)
    _qualifiedName = EAttribute(eType=EString, unique=False, derived=True,
                                changeable=False, name='qualifiedName', transient=True)

    @property
    def qualifiedName(self):
        raise NotImplementedError('Missing implementation for qualifiedName')

    def __init__(self, *, name=None, qualifiedName=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if qualifiedName is not None:
            self.qualifiedName = qualifiedName

    def getNamedContainer(self):

        raise NotImplementedError('operation getNamedContainer(...) not yet implemented')

    def getNamePrefix(self):

        raise NotImplementedError('operation getNamePrefix(...) not yet implemented')

    def getQualifiedNameSegments(self):

        raise NotImplementedError('operation getQualifiedNameSegments(...) not yet implemented')

    def getDefaultNameSeparator(self):
        """Overwrite this method to define a specific name separator."""
        raise NotImplementedError('operation getDefaultNameSeparator(...) not yet implemented')

    def getNamespace(self):

        raise NotImplementedError('operation getNamespace(...) not yet implemented')

    def getNamePrefixSegments(self):
        """Overwrite this method to define a specific prefix (used by name-based references)."""
        raise NotImplementedError('operation getNamePrefixSegments(...) not yet implemented')


@abstract
class IDisplayName(EObject, metaclass=MetaEClass):

    displayName = EAttribute(eType=EString, unique=False, derived=False, changeable=True)

    def __init__(self, *, displayName=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if displayName is not None:
            self.displayName = displayName

@abstract
class IDescription(EObject, metaclass=MetaEClass):

    description = EAttribute(eType=EString, unique=False, derived=False, changeable=True)

    def __init__(self, *, description=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if description is not None:
            self.description = description


@abstract
class INamespaceMember(EObject, metaclass=MetaEClass):

    namespace = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, namespace=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if namespace is not None:
            self.namespace = namespace


class TransmissionPolicy(EObject, metaclass=MetaEClass):
    """Data transmission details for communication (e.g. LabelAccesses)"""
    chunkProcessingTicks = EAttribute(eType=EInt, unique=False,
                                      derived=False, changeable=True, default_value='0')
    transmitRatio = EAttribute(eType=EDouble, unique=False, derived=False,
                               changeable=True, default_value='1.0')
    chunkSize = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, chunkSize=None, chunkProcessingTicks=None, transmitRatio=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if chunkProcessingTicks is not None:
            self.chunkProcessingTicks = chunkProcessingTicks

        if transmitRatio is not None:
            self.transmitRatio = transmitRatio

        if chunkSize is not None:
            self.chunkSize = chunkSize


@abstract
class Quantity(EObject, metaclass=MetaEClass):
    """Abstract class for Quantities (value + unit)"""

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class TimeComparable(EObject, metaclass=MetaEClass):

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class DataRateComparable(EObject, metaclass=MetaEClass):

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


class CustomProperty(EObject, metaclass=MetaEClass):
    """custom property container for map"""
    key = EAttribute(eType=EString, unique=False, derived=False, changeable=True)
    value = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, key=None, value=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if key is not None:
            self.key = key

        if value is not None:
            self.value = value


@abstract
class Value(EObject, metaclass=MetaEClass):
    """Abstract generalization of a value entry."""

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class NumericStatistic(EObject, metaclass=MetaEClass):

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class ITimeDeviation(EObject, metaclass=MetaEClass):

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

    def getLowerBound(self):

        raise NotImplementedError('operation getLowerBound(...) not yet implemented')

    def getUpperBound(self):

        raise NotImplementedError('operation getUpperBound(...) not yet implemented')

    def getAverage(self):

        raise NotImplementedError('operation getAverage(...) not yet implemented')


@abstract
class TimeInterval(EObject, metaclass=MetaEClass):

    lowerBound = EReference(ordered=True, unique=True, containment=True, derived=False)
    upperBound = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, lowerBound=None, upperBound=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if lowerBound is not None:
            self.lowerBound = lowerBound

        if upperBound is not None:
            self.upperBound = upperBound

    def getAverage(self):

        raise NotImplementedError('operation getAverage(...) not yet implemented')

    def validateInvariants(self, diagnostics=None, context=None):

        raise NotImplementedError('operation validateInvariants(...) not yet implemented')


@abstract
class IDiscreteValueDeviation(EObject, metaclass=MetaEClass):

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

    def getLowerBound(self):

        raise NotImplementedError('operation getLowerBound(...) not yet implemented')

    def getUpperBound(self):

        raise NotImplementedError('operation getUpperBound(...) not yet implemented')

    def getAverage(self):

        raise NotImplementedError('operation getAverage(...) not yet implemented')


@abstract
class DiscreteValueInterval(EObject, metaclass=MetaEClass):

    lowerBound = EAttribute(eType=ELongObject, unique=False, derived=False,
                            changeable=True, default_value='0')
    upperBound = EAttribute(eType=ELongObject, unique=False, derived=False,
                            changeable=True, default_value='0')

    def __init__(self, *, lowerBound=None, upperBound=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if lowerBound is not None:
            self.lowerBound = lowerBound

        if upperBound is not None:
            self.upperBound = upperBound

    def getAverage(self):

        raise NotImplementedError('operation getAverage(...) not yet implemented')

    def validateInvariants(self, diagnostics=None, context=None):

        raise NotImplementedError('operation validateInvariants(...) not yet implemented')


@abstract
class IContinuousValueDeviation(EObject, metaclass=MetaEClass):

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

    def getLowerBound(self):

        raise NotImplementedError('operation getLowerBound(...) not yet implemented')

    def getUpperBound(self):

        raise NotImplementedError('operation getUpperBound(...) not yet implemented')

    def getAverage(self):

        raise NotImplementedError('operation getAverage(...) not yet implemented')


@abstract
class ContinuousValueInterval(EObject, metaclass=MetaEClass):

    lowerBound = EAttribute(eType=EDoubleObject, unique=False, derived=False,
                            changeable=True, default_value='0.0')
    upperBound = EAttribute(eType=EDoubleObject, unique=False, derived=False,
                            changeable=True, default_value='0.0')

    def __init__(self, *, lowerBound=None, upperBound=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if lowerBound is not None:
            self.lowerBound = lowerBound

        if upperBound is not None:
            self.upperBound = upperBound

    def getAverage(self):

        raise NotImplementedError('operation getAverage(...) not yet implemented')

    def validateInvariants(self, diagnostics=None, context=None):

        raise NotImplementedError('operation validateInvariants(...) not yet implemented')


@abstract
class IComponentContainer(EObject, metaclass=MetaEClass):

    components = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, components=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if components:
            self.components.extend(components)


@abstract
class IInterfaceContainer(EObject, metaclass=MetaEClass):

    interfaces = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, interfaces=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if interfaces:
            self.interfaces.extend(interfaces)


class DerivedInnerports(EDerivedCollection):
    pass


@abstract
class ISystem(EObject, metaclass=MetaEClass):

    componentInstances = EReference(ordered=True, unique=True,
                                    containment=True, derived=False, upper=-1)
    connectors = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    groundedPorts = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    innerPorts = EReference(ordered=True, unique=True, containment=False,
                            derived=True, upper=-1, transient=True, derived_class=DerivedInnerports)

    def __init__(self, *, componentInstances=None, connectors=None, groundedPorts=None, innerPorts=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if componentInstances:
            self.componentInstances.extend(componentInstances)

        if connectors:
            self.connectors.extend(connectors)

        if groundedPorts:
            self.groundedPorts.extend(groundedPorts)

        if innerPorts:
            self.innerPorts.extend(innerPorts)


@abstract
class IComponentStructureMember(EObject, metaclass=MetaEClass):

    structure = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, structure=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if structure is not None:
            self.structure = structure


class InterfaceChannel(EObject, metaclass=MetaEClass):

    key = EReference(ordered=True, unique=True, containment=False, derived=False)
    value = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, key=None, value=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if key is not None:
            self.key = key

        if value is not None:
            self.value = value


@abstract
class ProcessConstraint(EObject, metaclass=MetaEClass):
    """An abstract superclass for all process related constraint
The target describes the entity on which the processes can be mapped"""
    target = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, target=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if target is not None:
            self.target = target


@abstract
class RunnableConstraint(EObject, metaclass=MetaEClass):
    """An abstract superclass for all runnable related constraint
The target describes the entity on which the runnables can be mapped"""
    target = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, target=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if target is not None:
            self.target = target


@abstract
class DataConstraint(EObject, metaclass=MetaEClass):
    """An abstract superclass for all data related constraint
The target describes the entity on which the data can be mapped"""
    target = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, target=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if target is not None:
            self.target = target


@abstract
class RunnableConstraintTarget(EObject, metaclass=MetaEClass):
    """An abstract superclass for all possible targets for runnable-constraints"""

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class ProcessConstraintTarget(EObject, metaclass=MetaEClass):
    """An abstract superclass for all possible targets for process-constraints"""

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class DataConstraintTarget(EObject, metaclass=MetaEClass):
    """An abstract superclass for all possible targets for data-constraints"""

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class LabelGroup(EObject, metaclass=MetaEClass):
    """An abstract description for a group of labels that can be paired or separated by a runnable-constraint"""

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class RunnableGroup(EObject, metaclass=MetaEClass):
    """An abstract description for a group of runnables that can be paired or separated by a runnable-constraint"""

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class ProcessGroup(EObject, metaclass=MetaEClass):
    """An abstract description for a group of processes that can be paired or separated by a process-constraint"""

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class EventChainItem(EObject, metaclass=MetaEClass):

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

    def getEventChain(self):

        raise NotImplementedError('operation getEventChain(...) not yet implemented')


@abstract
class DataAge(EObject, metaclass=MetaEClass):

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class RequirementLimit(EObject, metaclass=MetaEClass):

    limitType = EAttribute(eType=LimitType, unique=False, derived=False, changeable=True)

    def __init__(self, *, limitType=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if limitType is not None:
            self.limitType = limitType


@abstract
class DataGroupScope(EObject, metaclass=MetaEClass):

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class HwPath(EObject, metaclass=MetaEClass):

    _source = EReference(ordered=True, unique=True, containment=False,
                         derived=True, name='source', transient=True)
    _destination = EReference(ordered=True, unique=True, containment=False,
                              derived=True, name='destination', transient=True)

    @property
    def source(self):
        raise NotImplementedError('Missing implementation for source')

    @property
    def destination(self):
        raise NotImplementedError('Missing implementation for destination')

    def __init__(self, *, source=None, destination=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if source is not None:
            self.source = source

        if destination is not None:
            self.destination = destination

    def getContainingAccessElement(self):

        raise NotImplementedError('operation getContainingAccessElement(...) not yet implemented')


class DataStability(EObject, metaclass=MetaEClass):

    enabled = EAttribute(eType=EBoolean, unique=False, derived=False,
                         changeable=True, default_value='false')
    algorithm = EAttribute(eType=EString, unique=False, derived=False, changeable=True)
    accessMultiplicity = EAttribute(eType=AccessMultiplicity,
                                    unique=False, derived=False, changeable=True)
    level = EAttribute(eType=DataStabilityLevel, unique=False, derived=False, changeable=True)

    def __init__(self, *, enabled=None, algorithm=None, accessMultiplicity=None, level=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if enabled is not None:
            self.enabled = enabled

        if algorithm is not None:
            self.algorithm = algorithm

        if accessMultiplicity is not None:
            self.accessMultiplicity = accessMultiplicity

        if level is not None:
            self.level = level


class NonAtomicDataCoherency(EObject, metaclass=MetaEClass):

    enabled = EAttribute(eType=EBoolean, unique=False, derived=False,
                         changeable=True, default_value='false')
    algorithm = EAttribute(eType=EString, unique=False, derived=False, changeable=True)
    accessMultiplicity = EAttribute(eType=AccessMultiplicity,
                                    unique=False, derived=False, changeable=True)

    def __init__(self, *, enabled=None, algorithm=None, accessMultiplicity=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if enabled is not None:
            self.enabled = enabled

        if algorithm is not None:
            self.algorithm = algorithm

        if accessMultiplicity is not None:
            self.accessMultiplicity = accessMultiplicity


@abstract
class ISchedulingParameterContainer(EObject, metaclass=MetaEClass):

    schedulingParameters = EReference(ordered=True, unique=True,
                                      containment=True, derived=False, upper=-1)

    def __init__(self, *, schedulingParameters=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if schedulingParameters:
            self.schedulingParameters.extend(schedulingParameters)


class SchedulingParameter(EObject, metaclass=MetaEClass):

    key = EReference(ordered=True, unique=True, containment=False, derived=False)
    value = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, key=None, value=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if key is not None:
            self.key = key

        if value is not None:
            self.value = value


class ModeValueMapEntry(EObject, metaclass=MetaEClass):

    value = EAttribute(eType=EString, unique=False, derived=False, changeable=True)
    key = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, key=None, value=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if value is not None:
            self.value = value

        if key is not None:
            self.key = key


@abstract
class ISatisfiable(EObject, metaclass=MetaEClass):

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

    def isSatisfiedBy(self, context=None):

        raise NotImplementedError('operation isSatisfiedBy(...) not yet implemented')


@abstract
class ConditionDisjunctionEntry(EObject, metaclass=MetaEClass):

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class FixedPeriodic(EObject, metaclass=MetaEClass):
    """Stimulus that is triggered periodically.
offset: Time of first occurrence
recurrence: Time between following occurrences"""
    recurrence = EReference(ordered=True, unique=True, containment=True, derived=False)
    offset = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, recurrence=None, offset=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if recurrence is not None:
            self.recurrence = recurrence

        if offset is not None:
            self.offset = offset


@abstract
class IExecutable(EObject, metaclass=MetaEClass):
    """@since 1.2"""
    localLabels = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    activityGraph = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, localLabels=None, activityGraph=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if localLabels:
            self.localLabels.extend(localLabels)

        if activityGraph is not None:
            self.activityGraph = activityGraph


@abstract
class IActivityGraphItemContainer(EObject, metaclass=MetaEClass):

    items = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, items=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if items:
            self.items.extend(items)


@abstract
class IDependsOn(EObject, metaclass=MetaEClass):

    dependsOn = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, dependsOn=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if dependsOn is not None:
            self.dependsOn = dependsOn


class NeedEntry(EObject, metaclass=MetaEClass):

    key = EAttribute(eType=EString, unique=False, derived=False, changeable=True)
    value = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, key=None, value=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if key is not None:
            self.key = key

        if value is not None:
            self.value = value


class TicksEntry(EObject, metaclass=MetaEClass):

    key = EReference(ordered=True, unique=True, containment=False, derived=False)
    value = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, key=None, value=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if key is not None:
            self.key = key

        if value is not None:
            self.value = value


@abstract
class DataType(EObject, metaclass=MetaEClass):
    """Central access point for different data type definitions"""

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class LocalModeValue(EObject, metaclass=MetaEClass):

    label = EReference(ordered=True, unique=True, containment=False, derived=False)
    valueSource = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, label=None, valueSource=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if label is not None:
            self.label = label

        if valueSource is not None:
            self.valueSource = valueSource

    def validateInvariants(self, diagnostics=None, context=None):

        raise NotImplementedError('operation validateInvariants(...) not yet implemented')


@abstract
class ILocalModeValueSource(EObject, metaclass=MetaEClass):

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

    def isEnum(self):

        raise NotImplementedError('operation isEnum(...) not yet implemented')

    def isNumeric(self):

        raise NotImplementedError('operation isNumeric(...) not yet implemented')

    def getMode(self):

        raise NotImplementedError('operation getMode(...) not yet implemented')


@abstract
class BaseObject(IAnnotatable):
    """Base classes to be used to provide common functionality for all objects.
Needs to be extended by other classes."""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class IReferable(INamed):
    """IReferable: Computed ID for name based references"""
    _uniqueName = EAttribute(eType=EString, unique=False, derived=True,
                             changeable=False, iD=True, name='uniqueName', transient=True)

    @property
    def uniqueName(self):
        raise NotImplementedError('Missing implementation for uniqueName')

    def __init__(self, *, uniqueName=None, **kwargs):

        super().__init__(**kwargs)

        if uniqueName is not None:
            self.uniqueName = uniqueName

    def getEncodedQualifiedName(self):

        raise NotImplementedError('operation getEncodedQualifiedName(...) not yet implemented')

    def validateInvariants(self, diagnostics=None, context=None):

        raise NotImplementedError('operation validateInvariants(...) not yet implemented')


class Frequency(Quantity):
    """General frequency class to define frequency value and unit"""
    value = EAttribute(eType=NonNegativeDouble, unique=False,
                       derived=False, changeable=True, default_value='0.0')
    unit = EAttribute(eType=FrequencyUnit, unique=False, derived=False, changeable=True)

    def __init__(self, *, value=None, unit=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

        if unit is not None:
            self.unit = unit

    def toString(self):

        raise NotImplementedError('operation toString(...) not yet implemented')


class Voltage(Quantity):
    """General voltage class to define voltage value and unit"""
    value = EAttribute(eType=EDouble, unique=False, derived=False,
                       changeable=True, default_value='0.0')
    unit = EAttribute(eType=VoltageUnit, unique=False, derived=False, changeable=True)

    def __init__(self, *, value=None, unit=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

        if unit is not None:
            self.unit = unit

    def toString(self):

        raise NotImplementedError('operation toString(...) not yet implemented')


class DataSize(Quantity):
    """General data size class to define size (value and unit)"""
    value = EAttribute(eType=EBigInteger, unique=False, derived=False,
                       changeable=True, default_value='0')
    unit = EAttribute(eType=DataSizeUnit, unique=False, derived=False, changeable=True)

    def __init__(self, *, value=None, unit=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

        if unit is not None:
            self.unit = unit

    def toString(self):

        raise NotImplementedError('operation toString(...) not yet implemented')

    def getNumberBits(self):
        """Convenience methods to retrieve the size in Bits and Bytes"""
        raise NotImplementedError('operation getNumberBits(...) not yet implemented')

    def getNumberBytes(self):

        raise NotImplementedError('operation getNumberBytes(...) not yet implemented')


class ListObject(Value):

    values = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, values=None, **kwargs):

        super().__init__(**kwargs)

        if values:
            self.values.extend(values)


class MapObject(Value):
    """@since 1.2"""
    entries = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, entries=None, **kwargs):

        super().__init__(**kwargs)

        if entries:
            self.entries.extend(entries)


class StringObject(Value):
    """Object for using the elementary datatype String as generic parameter."""
    value = EAttribute(eType=EString, unique=False, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class BigIntegerObject(Value):
    """Object for using the elementary datatype BigInteger as generic parameter."""
    value = EAttribute(eType=EBigInteger, unique=False, derived=False,
                       changeable=True, default_value='0')

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class ReferenceObject(Value):
    """Object for using object reference as generic parameter."""
    value = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class IntegerObject(Value):
    """Object for using the elementary datatype integer as generic parameter."""
    value = EAttribute(eType=EInt, unique=False, derived=False, changeable=True, default_value='0')

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class LongObject(Value):
    """Object for using the elementary datatype long as generic parameter."""
    value = EAttribute(eType=ELong, unique=False, derived=False, changeable=True, default_value='0')

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class FloatObject(Value):
    """Object for using the elementary datatype float as generic parameter."""
    value = EAttribute(eType=EFloat, unique=False, derived=False,
                       changeable=True, default_value='0.0')

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class DoubleObject(Value):
    """Object for using the elementary datatype double as generic parameter."""
    value = EAttribute(eType=EDouble, unique=False, derived=False,
                       changeable=True, default_value='0.0')

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class BooleanObject(Value):
    """Object for using the elementary datatype boolean as generic parameter."""
    value = EAttribute(eType=EBoolean, unique=False, derived=False,
                       changeable=True, default_value='false')

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class MinAvgMaxStatistic(NumericStatistic):
    """Statistic to provide capabilities for min, max and avg"""
    min = EAttribute(eType=EInt, unique=False, derived=False, changeable=True, default_value='0')
    avg = EAttribute(eType=EFloat, unique=False, derived=False, changeable=True, default_value='0f')
    max = EAttribute(eType=EInt, unique=False, derived=False, changeable=True, default_value='0')

    def __init__(self, *, min=None, avg=None, max=None, **kwargs):

        super().__init__(**kwargs)

        if min is not None:
            self.min = min

        if avg is not None:
            self.avg = avg

        if max is not None:
            self.max = max

    def validateInvariants(self, diagnostics=None, context=None):

        raise NotImplementedError('operation validateInvariants(...) not yet implemented')


class SingleValueStatistic(NumericStatistic):

    value = EAttribute(eType=EFloat, unique=False, derived=False,
                       changeable=True, default_value='0f')

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class TimeConstant(ITimeDeviation):

    value = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

    def getLowerBound(self):

        raise NotImplementedError('operation getLowerBound(...) not yet implemented')

    def getUpperBound(self):

        raise NotImplementedError('operation getUpperBound(...) not yet implemented')

    def getAverage(self):

        raise NotImplementedError('operation getAverage(...) not yet implemented')


class TimeHistogram(ITimeDeviation):

    entries = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, entries=None, **kwargs):

        super().__init__(**kwargs)

        if entries:
            self.entries.extend(entries)

    def getLowerBound(self):

        raise NotImplementedError('operation getLowerBound(...) not yet implemented')

    def getUpperBound(self):

        raise NotImplementedError('operation getUpperBound(...) not yet implemented')

    def getAverage(self):

        raise NotImplementedError('operation getAverage(...) not yet implemented')


class TimeHistogramEntry(TimeInterval):

    occurrences = EAttribute(eType=PositiveLong, unique=False,
                             derived=False, changeable=True, default_value='1')

    def __init__(self, *, occurrences=None, **kwargs):

        super().__init__(**kwargs)

        if occurrences is not None:
            self.occurrences = occurrences


@abstract
class TruncatedTimeDistribution(ITimeDeviation):

    lowerBound = EReference(ordered=True, unique=True, containment=True, derived=False)
    upperBound = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, lowerBound=None, upperBound=None, **kwargs):

        super().__init__(**kwargs)

        if lowerBound is not None:
            self.lowerBound = lowerBound

        if upperBound is not None:
            self.upperBound = upperBound

    def validateInvariants(self, diagnostics=None, context=None):

        raise NotImplementedError('operation validateInvariants(...) not yet implemented')


class DiscreteValueConstant(IDiscreteValueDeviation):

    value = EAttribute(eType=ELong, unique=False, derived=False, changeable=True, default_value='0')

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

    def getLowerBound(self):

        raise NotImplementedError('operation getLowerBound(...) not yet implemented')

    def getUpperBound(self):

        raise NotImplementedError('operation getUpperBound(...) not yet implemented')

    def getAverage(self):

        raise NotImplementedError('operation getAverage(...) not yet implemented')


class DiscreteValueHistogram(IDiscreteValueDeviation):

    entries = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, entries=None, **kwargs):

        super().__init__(**kwargs)

        if entries:
            self.entries.extend(entries)

    def getLowerBound(self):

        raise NotImplementedError('operation getLowerBound(...) not yet implemented')

    def getUpperBound(self):

        raise NotImplementedError('operation getUpperBound(...) not yet implemented')

    def getAverage(self):

        raise NotImplementedError('operation getAverage(...) not yet implemented')


class DiscreteValueHistogramEntry(DiscreteValueInterval):

    occurrences = EAttribute(eType=PositiveLong, unique=False,
                             derived=False, changeable=True, default_value='1')

    def __init__(self, *, occurrences=None, **kwargs):

        super().__init__(**kwargs)

        if occurrences is not None:
            self.occurrences = occurrences


@abstract
class TruncatedDiscreteValueDistribution(IDiscreteValueDeviation):

    lowerBound = EAttribute(eType=ELongObject, unique=False, derived=False, changeable=True)
    upperBound = EAttribute(eType=ELongObject, unique=False, derived=False, changeable=True)

    def __init__(self, *, lowerBound=None, upperBound=None, **kwargs):

        super().__init__(**kwargs)

        if lowerBound is not None:
            self.lowerBound = lowerBound

        if upperBound is not None:
            self.upperBound = upperBound

    def validateInvariants(self, diagnostics=None, context=None):

        raise NotImplementedError('operation validateInvariants(...) not yet implemented')


class ContinuousValueConstant(IContinuousValueDeviation):

    value = EAttribute(eType=EDouble, unique=False, derived=False,
                       changeable=True, default_value='0.0')

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

    def getLowerBound(self):

        raise NotImplementedError('operation getLowerBound(...) not yet implemented')

    def getUpperBound(self):

        raise NotImplementedError('operation getUpperBound(...) not yet implemented')

    def getAverage(self):

        raise NotImplementedError('operation getAverage(...) not yet implemented')


class ContinuousValueHistogram(IContinuousValueDeviation):

    entries = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, entries=None, **kwargs):

        super().__init__(**kwargs)

        if entries:
            self.entries.extend(entries)

    def getLowerBound(self):

        raise NotImplementedError('operation getLowerBound(...) not yet implemented')

    def getUpperBound(self):

        raise NotImplementedError('operation getUpperBound(...) not yet implemented')

    def getAverage(self):

        raise NotImplementedError('operation getAverage(...) not yet implemented')


class ContinuousValueHistogramEntry(ContinuousValueInterval):

    occurrences = EAttribute(eType=PositiveLong, unique=False,
                             derived=False, changeable=True, default_value='1')

    def __init__(self, *, occurrences=None, **kwargs):

        super().__init__(**kwargs)

        if occurrences is not None:
            self.occurrences = occurrences


@abstract
class TruncatedContinuousValueDistribution(IContinuousValueDeviation):

    lowerBound = EAttribute(eType=EDoubleObject, unique=False, derived=False, changeable=True)
    upperBound = EAttribute(eType=EDoubleObject, unique=False, derived=False, changeable=True)

    def __init__(self, *, lowerBound=None, upperBound=None, **kwargs):

        super().__init__(**kwargs)

        if lowerBound is not None:
            self.lowerBound = lowerBound

        if upperBound is not None:
            self.upperBound = upperBound

    def validateInvariants(self, diagnostics=None, context=None):

        raise NotImplementedError('operation validateInvariants(...) not yet implemented')


class DataAgeCycle(DataAge):

    minimumCycle = EAttribute(eType=EInt, unique=False, derived=False,
                              changeable=True, default_value='0')
    maximumCycle = EAttribute(eType=EInt, unique=False, derived=False,
                              changeable=True, default_value='0')

    def __init__(self, *, minimumCycle=None, maximumCycle=None, **kwargs):

        super().__init__(**kwargs)

        if minimumCycle is not None:
            self.minimumCycle = minimumCycle

        if maximumCycle is not None:
            self.maximumCycle = maximumCycle


class DataAgeTime(DataAge):

    minimumTime = EReference(ordered=True, unique=True, containment=True, derived=False)
    maximumTime = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, minimumTime=None, maximumTime=None, **kwargs):

        super().__init__(**kwargs)

        if minimumTime is not None:
            self.minimumTime = minimumTime

        if maximumTime is not None:
            self.maximumTime = maximumTime


class CPUPercentageRequirementLimit(RequirementLimit):

    metric = EAttribute(eType=CPUPercentageMetric, unique=False, derived=False, changeable=True)
    limitValue = EAttribute(eType=EDouble, unique=False, derived=False,
                            changeable=True, default_value='0.0')
    hardwareContext = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, metric=None, limitValue=None, hardwareContext=None, **kwargs):

        super().__init__(**kwargs)

        if metric is not None:
            self.metric = metric

        if limitValue is not None:
            self.limitValue = limitValue

        if hardwareContext is not None:
            self.hardwareContext = hardwareContext


class FrequencyRequirementLimit(RequirementLimit):

    metric = EAttribute(eType=FrequencyMetric, unique=False, derived=False, changeable=True)
    limitValue = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, metric=None, limitValue=None, **kwargs):

        super().__init__(**kwargs)

        if metric is not None:
            self.metric = metric

        if limitValue is not None:
            self.limitValue = limitValue


class PercentageRequirementLimit(RequirementLimit):

    metric = EAttribute(eType=PercentageMetric, unique=False, derived=False, changeable=True)
    limitValue = EAttribute(eType=EDouble, unique=False, derived=False,
                            changeable=True, default_value='0.0')

    def __init__(self, *, metric=None, limitValue=None, **kwargs):

        super().__init__(**kwargs)

        if metric is not None:
            self.metric = metric

        if limitValue is not None:
            self.limitValue = limitValue


class CountRequirementLimit(RequirementLimit):

    metric = EAttribute(eType=CountMetric, unique=False, derived=False, changeable=True)
    limitValue = EAttribute(eType=EInt, unique=False, derived=False,
                            changeable=True, default_value='0')

    def __init__(self, *, metric=None, limitValue=None, **kwargs):

        super().__init__(**kwargs)

        if metric is not None:
            self.metric = metric

        if limitValue is not None:
            self.limitValue = limitValue


class TimeRequirementLimit(RequirementLimit):

    metric = EAttribute(eType=TimeMetric, unique=False, derived=False, changeable=True)
    limitValue = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, metric=None, limitValue=None, **kwargs):

        super().__init__(**kwargs)

        if metric is not None:
            self.metric = metric

        if limitValue is not None:
            self.limitValue = limitValue


class ProcessScope(DataGroupScope):

    process = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, process=None, **kwargs):

        super().__init__(**kwargs)

        if process is not None:
            self.process = process


class RunnableScope(DataGroupScope):

    runnable = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, runnable=None, **kwargs):

        super().__init__(**kwargs)

        if runnable is not None:
            self.runnable = runnable


class ComponentScope(DataGroupScope):

    component = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, component=None, **kwargs):

        super().__init__(**kwargs)

        if component is not None:
            self.component = component


class SchedulerAssociation(ISchedulingParameterContainer):

    child = EReference(ordered=True, unique=True, containment=False, derived=False)
    parent = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, child=None, parent=None, **kwargs):

        super().__init__(**kwargs)

        if child is not None:
            self.child = child

        if parent is not None:
            self.parent = parent


@abstract
class ModeConditionDisjunctionEntry(ISatisfiable):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class Condition(ConditionDisjunctionEntry):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ModeLiteralConst(ILocalModeValueSource):

    value = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

    def isEnum(self):

        raise NotImplementedError('operation isEnum(...) not yet implemented')

    def getMode(self):

        raise NotImplementedError('operation getMode(...) not yet implemented')


class IntegerConst(ILocalModeValueSource):

    value = EAttribute(eType=EInt, unique=False, derived=False, changeable=True, default_value='0')

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

    def isNumeric(self):

        raise NotImplementedError('operation isNumeric(...) not yet implemented')


class ModeLabelRef(ILocalModeValueSource):

    value = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

    def isEnum(self):

        raise NotImplementedError('operation isEnum(...) not yet implemented')

    def isNumeric(self):

        raise NotImplementedError('operation isNumeric(...) not yet implemented')

    def getMode(self):

        raise NotImplementedError('operation getMode(...) not yet implemented')


class LocalModeLabelRef(ILocalModeValueSource):

    value = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

    def isEnum(self):

        raise NotImplementedError('operation isEnum(...) not yet implemented')

    def isNumeric(self):

        raise NotImplementedError('operation isNumeric(...) not yet implemented')

    def getMode(self):

        raise NotImplementedError('operation getMode(...) not yet implemented')


class ChannelFillRef(ILocalModeValueSource):

    value = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

    def isNumeric(self):

        raise NotImplementedError('operation isNumeric(...) not yet implemented')


class ArithmeticExpression(ILocalModeValueSource):

    operator = EAttribute(eType=ArithmeticOperator, unique=False, derived=False, changeable=True)
    operand1 = EReference(ordered=True, unique=True, containment=True, derived=False)
    operand2 = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, operand1=None, operand2=None, operator=None, **kwargs):

        super().__init__(**kwargs)

        if operator is not None:
            self.operator = operator

        if operand1 is not None:
            self.operand1 = operand1

        if operand2 is not None:
            self.operand2 = operand2

    def isNumeric(self):

        raise NotImplementedError('operation isNumeric(...) not yet implemented')


class Amalthea(BaseObject):

    _version = EAttribute(eType=EString, unique=False, derived=True,
                          changeable=False, name='version', transient=True)
    commonElements = EReference(ordered=True, unique=True, containment=True, derived=False)
    swModel = EReference(ordered=True, unique=True, containment=True, derived=False)
    hwModel = EReference(ordered=True, unique=True, containment=True, derived=False)
    osModel = EReference(ordered=True, unique=True, containment=True, derived=False)
    stimuliModel = EReference(ordered=True, unique=True, containment=True, derived=False)
    eventModel = EReference(ordered=True, unique=True, containment=True, derived=False)
    constraintsModel = EReference(ordered=True, unique=True, containment=True, derived=False)
    propertyConstraintsModel = EReference(
        ordered=True, unique=True, containment=True, derived=False)
    mappingModel = EReference(ordered=True, unique=True, containment=True, derived=False)
    componentsModel = EReference(ordered=True, unique=True, containment=True, derived=False)
    configModel = EReference(ordered=True, unique=True, containment=True, derived=False)

    @property
    def version(self):
        raise NotImplementedError('Missing implementation for version')

    def __init__(self, *, version=None, commonElements=None, swModel=None, hwModel=None, osModel=None, stimuliModel=None, eventModel=None, constraintsModel=None, propertyConstraintsModel=None, mappingModel=None, componentsModel=None, configModel=None, **kwargs):

        super().__init__(**kwargs)

        if version is not None:
            self.version = version

        if commonElements is not None:
            self.commonElements = commonElements

        if swModel is not None:
            self.swModel = swModel

        if hwModel is not None:
            self.hwModel = hwModel

        if osModel is not None:
            self.osModel = osModel

        if stimuliModel is not None:
            self.stimuliModel = stimuliModel

        if eventModel is not None:
            self.eventModel = eventModel

        if constraintsModel is not None:
            self.constraintsModel = constraintsModel

        if propertyConstraintsModel is not None:
            self.propertyConstraintsModel = propertyConstraintsModel

        if mappingModel is not None:
            self.mappingModel = mappingModel

        if componentsModel is not None:
            self.componentsModel = componentsModel

        if configModel is not None:
            self.configModel = configModel


class CommonElements(BaseObject):

    tags = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    namespaces = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    coreClassifiers = EReference(ordered=True, unique=True,
                                 containment=True, derived=False, upper=-1)
    memoryClassifiers = EReference(ordered=True, unique=True,
                                   containment=True, derived=False, upper=-1)

    def __init__(self, *, tags=None, namespaces=None, coreClassifiers=None, memoryClassifiers=None, **kwargs):

        super().__init__(**kwargs)

        if tags:
            self.tags.extend(tags)

        if namespaces:
            self.namespaces.extend(namespaces)

        if coreClassifiers:
            self.coreClassifiers.extend(coreClassifiers)

        if memoryClassifiers:
            self.memoryClassifiers.extend(memoryClassifiers)


@abstract
class ReferableObject(IReferable):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DataRate(Quantity, DataRateComparable):
    """General data rate class to define rate (value and unit)"""
    value = EAttribute(eType=EBigInteger, unique=False, derived=False,
                       changeable=True, default_value='0')
    unit = EAttribute(eType=DataRateUnit, unique=False, derived=False, changeable=True)

    def __init__(self, *, value=None, unit=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

        if unit is not None:
            self.unit = unit

    def toString(self):

        raise NotImplementedError('operation toString(...) not yet implemented')

    def compareTo(self, rate=None):

        raise NotImplementedError('operation compareTo(...) not yet implemented')


@abstract
class BoundedTimeDistribution(TimeInterval, ITimeDeviation):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class TimeGaussDistribution(TruncatedTimeDistribution):
    """Gauss distribution"""
    mean = EReference(ordered=True, unique=True, containment=True, derived=False)
    sd = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, mean=None, sd=None, **kwargs):

        super().__init__(**kwargs)

        if mean is not None:
            self.mean = mean

        if sd is not None:
            self.sd = sd

    def getAverage(self):

        raise NotImplementedError('operation getAverage(...) not yet implemented')


@abstract
class BoundedDiscreteValueDistribution(DiscreteValueInterval, IDiscreteValueDeviation):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DiscreteValueGaussDistribution(TruncatedDiscreteValueDistribution):
    """Gauss distribution"""
    mean = EAttribute(eType=EDouble, unique=False, derived=False,
                      changeable=True, default_value='0.0')
    sd = EAttribute(eType=PositiveDouble, unique=False, derived=False,
                    changeable=True, default_value='1.0')

    def __init__(self, *, mean=None, sd=None, **kwargs):

        super().__init__(**kwargs)

        if mean is not None:
            self.mean = mean

        if sd is not None:
            self.sd = sd

    def getAverage(self):

        raise NotImplementedError('operation getAverage(...) not yet implemented')


@abstract
class BoundedContinuousValueDistribution(ContinuousValueInterval, IContinuousValueDeviation):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ContinuousValueGaussDistribution(TruncatedContinuousValueDistribution):
    """Gauss distribution"""
    mean = EAttribute(eType=EDouble, unique=False, derived=False,
                      changeable=True, default_value='0.0')
    sd = EAttribute(eType=PositiveDouble, unique=False, derived=False,
                    changeable=True, default_value='1.0')

    def __init__(self, *, mean=None, sd=None, **kwargs):

        super().__init__(**kwargs)

        if mean is not None:
            self.mean = mean

        if sd is not None:
            self.sd = sd

    def getAverage(self):

        raise NotImplementedError('operation getAverage(...) not yet implemented')


class QualifiedPort(BaseObject):

    instance = EReference(ordered=True, unique=True, containment=False, derived=False)
    port = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, instance=None, port=None, **kwargs):

        super().__init__(**kwargs)

        if instance is not None:
            self.instance = instance

        if port is not None:
            self.port = port


class ConfigModel(BaseObject):

    eventsToTrace = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, eventsToTrace=None, **kwargs):

        super().__init__(**kwargs)

        if eventsToTrace:
            self.eventsToTrace.extend(eventsToTrace)


class ConstraintsModel(BaseObject):

    eventChains = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    timingConstraints = EReference(ordered=True, unique=True,
                                   containment=True, derived=False, upper=-1)
    affinityConstraints = EReference(ordered=True, unique=True,
                                     containment=True, derived=False, upper=-1)
    runnableSequencingConstraints = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    dataAgeConstraints = EReference(ordered=True, unique=True,
                                    containment=True, derived=False, upper=-1)
    requirements = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    dataCoherencyGroups = EReference(ordered=True, unique=True,
                                     containment=True, derived=False, upper=-1)
    dataStabilityGroups = EReference(ordered=True, unique=True,
                                     containment=True, derived=False, upper=-1)
    physicalSectionConstraints = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, eventChains=None, timingConstraints=None, affinityConstraints=None, runnableSequencingConstraints=None, dataAgeConstraints=None, requirements=None, dataCoherencyGroups=None, dataStabilityGroups=None, physicalSectionConstraints=None, **kwargs):

        super().__init__(**kwargs)

        if eventChains:
            self.eventChains.extend(eventChains)

        if timingConstraints:
            self.timingConstraints.extend(timingConstraints)

        if affinityConstraints:
            self.affinityConstraints.extend(affinityConstraints)

        if runnableSequencingConstraints:
            self.runnableSequencingConstraints.extend(runnableSequencingConstraints)

        if dataAgeConstraints:
            self.dataAgeConstraints.extend(dataAgeConstraints)

        if requirements:
            self.requirements.extend(requirements)

        if dataCoherencyGroups:
            self.dataCoherencyGroups.extend(dataCoherencyGroups)

        if dataStabilityGroups:
            self.dataStabilityGroups.extend(dataStabilityGroups)

        if physicalSectionConstraints:
            self.physicalSectionConstraints.extend(physicalSectionConstraints)


class EventModel(BaseObject):

    events = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, events=None, **kwargs):

        super().__init__(**kwargs)

        if events:
            self.events.extend(events)


class HWModel(BaseObject):

    definitions = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    featureCategories = EReference(ordered=True, unique=True,
                                   containment=True, derived=False, upper=-1)
    structures = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    domains = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, definitions=None, featureCategories=None, structures=None, domains=None, **kwargs):

        super().__init__(**kwargs)

        if definitions:
            self.definitions.extend(definitions)

        if featureCategories:
            self.featureCategories.extend(featureCategories)

        if structures:
            self.structures.extend(structures)

        if domains:
            self.domains.extend(domains)


class HwAccessElement(ITaggable, INamed):

    source = EReference(ordered=True, unique=True, containment=False, derived=False)
    destination = EReference(ordered=True, unique=True, containment=False, derived=False)
    accessPath = EReference(ordered=True, unique=True, containment=True, derived=False)
    readLatency = EReference(ordered=True, unique=True, containment=True, derived=False)
    writeLatency = EReference(ordered=True, unique=True, containment=True, derived=False)
    dataRate = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, source=None, destination=None, accessPath=None, readLatency=None, writeLatency=None, dataRate=None, **kwargs):

        super().__init__(**kwargs)

        if source is not None:
            self.source = source

        if destination is not None:
            self.destination = destination

        if accessPath is not None:
            self.accessPath = accessPath

        if readLatency is not None:
            self.readLatency = readLatency

        if writeLatency is not None:
            self.writeLatency = writeLatency

        if dataRate is not None:
            self.dataRate = dataRate


class HwAccessPath(HwPath, INamed):

    startAddress = EAttribute(eType=Address, unique=False, derived=False,
                              changeable=True, default_value='0')
    endAddress = EAttribute(eType=Address, unique=False, derived=False,
                            changeable=True, default_value='0')
    memOffset = EAttribute(eType=Address, unique=False, derived=False,
                           changeable=True, default_value='0')
    containingAccessElement = EReference(
        ordered=True, unique=True, containment=False, derived=False)
    pathElements = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, containingAccessElement=None, pathElements=None, startAddress=None, endAddress=None, memOffset=None, **kwargs):

        super().__init__(**kwargs)

        if startAddress is not None:
            self.startAddress = startAddress

        if endAddress is not None:
            self.endAddress = endAddress

        if memOffset is not None:
            self.memOffset = memOffset

        if containingAccessElement is not None:
            self.containingAccessElement = containingAccessElement

        if pathElements:
            self.pathElements.extend(pathElements)


@abstract
class HwPathElement(IReferable):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

    def getPorts(self):

        raise NotImplementedError('operation getPorts(...) not yet implemented')


@abstract
class HwDestination(IReferable):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

    def getPorts(self):

        raise NotImplementedError('operation getPorts(...) not yet implemented')


class MappingModel(BaseObject):

    addressMappingType = EAttribute(eType=MemoryAddressMappingType,
                                    unique=False, derived=False, changeable=True)
    schedulerAllocation = EReference(ordered=True, unique=True,
                                     containment=True, derived=False, upper=-1)
    runnableAllocation = EReference(ordered=True, unique=True,
                                    containment=True, derived=False, upper=-1)
    taskAllocation = EReference(ordered=True, unique=True,
                                containment=True, derived=False, upper=-1)
    isrAllocation = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    memoryMapping = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    physicalSectionMapping = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, schedulerAllocation=None, runnableAllocation=None, taskAllocation=None, isrAllocation=None, memoryMapping=None, physicalSectionMapping=None, addressMappingType=None, **kwargs):

        super().__init__(**kwargs)

        if addressMappingType is not None:
            self.addressMappingType = addressMappingType

        if schedulerAllocation:
            self.schedulerAllocation.extend(schedulerAllocation)

        if runnableAllocation:
            self.runnableAllocation.extend(runnableAllocation)

        if taskAllocation:
            self.taskAllocation.extend(taskAllocation)

        if isrAllocation:
            self.isrAllocation.extend(isrAllocation)

        if memoryMapping:
            self.memoryMapping.extend(memoryMapping)

        if physicalSectionMapping:
            self.physicalSectionMapping.extend(physicalSectionMapping)


class SchedulerAllocation(BaseObject):
    """Allocation of Schedulers"""
    scheduler = EReference(ordered=True, unique=True, containment=False, derived=False)
    responsibility = EReference(ordered=True, unique=True,
                                containment=False, derived=False, upper=-1)
    executingPU = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, scheduler=None, responsibility=None, executingPU=None, **kwargs):

        super().__init__(**kwargs)

        if scheduler is not None:
            self.scheduler = scheduler

        if responsibility:
            self.responsibility.extend(responsibility)

        if executingPU is not None:
            self.executingPU = executingPU


class ISRAllocation(BaseObject):

    priority = EAttribute(eType=EIntegerObject, unique=False, derived=False, changeable=True)
    isr = EReference(ordered=True, unique=True, containment=False, derived=False)
    controller = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, isr=None, controller=None, priority=None, **kwargs):

        super().__init__(**kwargs)

        if priority is not None:
            self.priority = priority

        if isr is not None:
            self.isr = isr

        if controller is not None:
            self.controller = controller


class RunnableAllocation(BaseObject):

    scheduler = EReference(ordered=True, unique=True, containment=False, derived=False)
    entity = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, scheduler=None, entity=None, **kwargs):

        super().__init__(**kwargs)

        if scheduler is not None:
            self.scheduler = scheduler

        if entity is not None:
            self.entity = entity


class MemoryMapping(BaseObject):
    """Mapping of AbstractMemoryElement (Label, Runnable, ISR, Task, ...)
to a specific memory."""
    memoryPositionAddress = EAttribute(
        eType=Address, unique=False, derived=False, changeable=True, default_value='0')
    abstractElement = EReference(ordered=True, unique=True, containment=False, derived=False)
    memory = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, abstractElement=None, memory=None, memoryPositionAddress=None, **kwargs):

        super().__init__(**kwargs)

        if memoryPositionAddress is not None:
            self.memoryPositionAddress = memoryPositionAddress

        if abstractElement is not None:
            self.abstractElement = abstractElement

        if memory is not None:
            self.memory = memory


class OSModel(BaseObject):

    semaphores = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    operatingSystems = EReference(ordered=True, unique=True,
                                  containment=True, derived=False, upper=-1)
    osOverheads = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    schedulerDefinitions = EReference(ordered=True, unique=True,
                                      containment=True, derived=False, upper=-1)
    schedulingParameterDefinitions = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, semaphores=None, operatingSystems=None, osOverheads=None, schedulerDefinitions=None, schedulingParameterDefinitions=None, **kwargs):

        super().__init__(**kwargs)

        if semaphores:
            self.semaphores.extend(semaphores)

        if operatingSystems:
            self.operatingSystems.extend(operatingSystems)

        if osOverheads:
            self.osOverheads.extend(osOverheads)

        if schedulerDefinitions:
            self.schedulerDefinitions.extend(schedulerDefinitions)

        if schedulingParameterDefinitions:
            self.schedulingParameterDefinitions.extend(schedulingParameterDefinitions)


class OsDataConsistency(BaseObject):

    mode = EAttribute(eType=OsDataConsistencyMode, unique=False, derived=False, changeable=True)
    dataStability = EReference(ordered=True, unique=True, containment=True, derived=False)
    nonAtomicDataCoherency = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, mode=None, dataStability=None, nonAtomicDataCoherency=None, **kwargs):

        super().__init__(**kwargs)

        if mode is not None:
            self.mode = mode

        if dataStability is not None:
            self.dataStability = dataStability

        if nonAtomicDataCoherency is not None:
            self.nonAtomicDataCoherency = nonAtomicDataCoherency


class OsAPIOverhead(BaseObject):

    apiSendMessage = EReference(ordered=True, unique=True, containment=True, derived=False)
    apiTerminateTask = EReference(ordered=True, unique=True, containment=True, derived=False)
    apiSchedule = EReference(ordered=True, unique=True, containment=True, derived=False)
    apiRequestResource = EReference(ordered=True, unique=True, containment=True, derived=False)
    apiReleaseResource = EReference(ordered=True, unique=True, containment=True, derived=False)
    apiSetEvent = EReference(ordered=True, unique=True, containment=True, derived=False)
    apiWaitEvent = EReference(ordered=True, unique=True, containment=True, derived=False)
    apiClearEvent = EReference(ordered=True, unique=True, containment=True, derived=False)
    apiActivateTask = EReference(ordered=True, unique=True, containment=True, derived=False)
    apiEnforcedMigration = EReference(ordered=True, unique=True, containment=True, derived=False)
    apiSuspendOsInterrupts = EReference(ordered=True, unique=True, containment=True, derived=False)
    apiResumeOsInterrupts = EReference(ordered=True, unique=True, containment=True, derived=False)
    apiRequestSpinlock = EReference(ordered=True, unique=True, containment=True, derived=False)
    apiReleaseSpinlock = EReference(ordered=True, unique=True, containment=True, derived=False)
    apiSenderReceiverRead = EReference(ordered=True, unique=True, containment=True, derived=False)
    apiSenderReceiverWrite = EReference(ordered=True, unique=True, containment=True, derived=False)
    apiSynchronousServerCallPoint = EReference(
        ordered=True, unique=True, containment=True, derived=False)
    apiIocRead = EReference(ordered=True, unique=True, containment=True, derived=False)
    apiIocWrite = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, apiSendMessage=None, apiTerminateTask=None, apiSchedule=None, apiRequestResource=None, apiReleaseResource=None, apiSetEvent=None, apiWaitEvent=None, apiClearEvent=None, apiActivateTask=None, apiEnforcedMigration=None, apiSuspendOsInterrupts=None, apiResumeOsInterrupts=None, apiRequestSpinlock=None, apiReleaseSpinlock=None, apiSenderReceiverRead=None, apiSenderReceiverWrite=None, apiSynchronousServerCallPoint=None, apiIocRead=None, apiIocWrite=None, **kwargs):

        super().__init__(**kwargs)

        if apiSendMessage is not None:
            self.apiSendMessage = apiSendMessage

        if apiTerminateTask is not None:
            self.apiTerminateTask = apiTerminateTask

        if apiSchedule is not None:
            self.apiSchedule = apiSchedule

        if apiRequestResource is not None:
            self.apiRequestResource = apiRequestResource

        if apiReleaseResource is not None:
            self.apiReleaseResource = apiReleaseResource

        if apiSetEvent is not None:
            self.apiSetEvent = apiSetEvent

        if apiWaitEvent is not None:
            self.apiWaitEvent = apiWaitEvent

        if apiClearEvent is not None:
            self.apiClearEvent = apiClearEvent

        if apiActivateTask is not None:
            self.apiActivateTask = apiActivateTask

        if apiEnforcedMigration is not None:
            self.apiEnforcedMigration = apiEnforcedMigration

        if apiSuspendOsInterrupts is not None:
            self.apiSuspendOsInterrupts = apiSuspendOsInterrupts

        if apiResumeOsInterrupts is not None:
            self.apiResumeOsInterrupts = apiResumeOsInterrupts

        if apiRequestSpinlock is not None:
            self.apiRequestSpinlock = apiRequestSpinlock

        if apiReleaseSpinlock is not None:
            self.apiReleaseSpinlock = apiReleaseSpinlock

        if apiSenderReceiverRead is not None:
            self.apiSenderReceiverRead = apiSenderReceiverRead

        if apiSenderReceiverWrite is not None:
            self.apiSenderReceiverWrite = apiSenderReceiverWrite

        if apiSynchronousServerCallPoint is not None:
            self.apiSynchronousServerCallPoint = apiSynchronousServerCallPoint

        if apiIocRead is not None:
            self.apiIocRead = apiIocRead

        if apiIocWrite is not None:
            self.apiIocWrite = apiIocWrite


class OsISROverhead(BaseObject):

    preExecutionOverhead = EReference(ordered=True, unique=True, containment=True, derived=False)
    postExecutionOverhead = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, preExecutionOverhead=None, postExecutionOverhead=None, **kwargs):

        super().__init__(**kwargs)

        if preExecutionOverhead is not None:
            self.preExecutionOverhead = preExecutionOverhead

        if postExecutionOverhead is not None:
            self.postExecutionOverhead = postExecutionOverhead


class PropertyConstraintsModel(BaseObject):

    allocationConstraints = EReference(ordered=True, unique=True,
                                       containment=True, derived=False, upper=-1)
    mappingConstraints = EReference(ordered=True, unique=True,
                                    containment=True, derived=False, upper=-1)

    def __init__(self, *, allocationConstraints=None, mappingConstraints=None, **kwargs):

        super().__init__(**kwargs)

        if allocationConstraints:
            self.allocationConstraints.extend(allocationConstraints)

        if mappingConstraints:
            self.mappingConstraints.extend(mappingConstraints)


@abstract
class CoreAllocationConstraint(BaseObject):
    """Abstract Class, used to describe Constraints for Allocations
(these usually target Cores and their features/attributes)"""
    coreClassification = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, coreClassification=None, **kwargs):

        super().__init__(**kwargs)

        if coreClassification is not None:
            self.coreClassification = coreClassification


@abstract
class MemoryMappingConstraint(BaseObject):
    """Abstract Class, used to describe Constraints for Mapping
(these usually target Memories and their features/attributes)"""
    memoryClassification = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, memoryClassification=None, **kwargs):

        super().__init__(**kwargs)

        if memoryClassification is not None:
            self.memoryClassification = memoryClassification


@abstract
class Classification(BaseObject):
    """Generalization for all Hardware related constraints"""
    condition = EAttribute(eType=CombinatorialCondition, unique=False,
                           derived=False, changeable=True)
    grouping = EAttribute(eType=GroupingType, unique=False, derived=False, changeable=True)

    def __init__(self, *, condition=None, grouping=None, **kwargs):

        super().__init__(**kwargs)

        if condition is not None:
            self.condition = condition

        if grouping is not None:
            self.grouping = grouping


class StimuliModel(BaseObject):

    stimuli = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    clocks = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, stimuli=None, clocks=None, **kwargs):

        super().__init__(**kwargs)

        if stimuli:
            self.stimuli.extend(stimuli)

        if clocks:
            self.clocks.extend(clocks)


class ModeValueList(BaseObject):

    entries = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, entries=None, **kwargs):

        super().__init__(**kwargs)

        if entries:
            self.entries.extend(entries)


@abstract
class ModeValue(BaseObject):

    value = EAttribute(eType=EString, unique=False, derived=False, changeable=True)
    label = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, label=None, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

        if label is not None:
            self.label = label

    def validateInvariants(self, diagnostics=None, context=None):

        raise NotImplementedError('operation validateInvariants(...) not yet implemented')

    def getLiteral(self):

        raise NotImplementedError('operation getLiteral(...) not yet implemented')

    def getInteger(self):

        raise NotImplementedError('operation getInteger(...) not yet implemented')


class ConditionDisjunction(BaseObject):

    entries = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, entries=None, **kwargs):

        super().__init__(**kwargs)

        if entries:
            self.entries.extend(entries)


class Scenario(BaseObject):

    samplingOffset = EAttribute(eType=NonNegativeDouble, unique=False,
                                derived=False, changeable=True, default_value='0.0')
    samplingRecurrence = EAttribute(eType=NonNegativeDouble, unique=False,
                                    derived=False, changeable=True, default_value='1.0')
    clock = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, clock=None, samplingOffset=None, samplingRecurrence=None, **kwargs):

        super().__init__(**kwargs)

        if samplingOffset is not None:
            self.samplingOffset = samplingOffset

        if samplingRecurrence is not None:
            self.samplingRecurrence = samplingRecurrence

        if clock is not None:
            self.clock = clock


class ArrivalCurveEntry(BaseObject):

    numberOfOccurrences = EAttribute(eType=PositiveInt, unique=False,
                                     derived=False, changeable=True, default_value='1')
    lowerTimeBorder = EReference(ordered=True, unique=True, containment=True, derived=False)
    upperTimeBorder = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, numberOfOccurrences=None, lowerTimeBorder=None, upperTimeBorder=None, **kwargs):

        super().__init__(**kwargs)

        if numberOfOccurrences is not None:
            self.numberOfOccurrences = numberOfOccurrences

        if lowerTimeBorder is not None:
            self.lowerTimeBorder = lowerTimeBorder

        if upperTimeBorder is not None:
            self.upperTimeBorder = upperTimeBorder


class ClockStep(BaseObject):

    frequency = EReference(ordered=True, unique=True, containment=True, derived=False)
    time = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, frequency=None, time=None, **kwargs):

        super().__init__(**kwargs)

        if frequency is not None:
            self.frequency = frequency

        if time is not None:
            self.time = time


class SWModel(BaseObject):
    """Central instance to provide central access."""
    isrs = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    tasks = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    runnables = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    labels = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    channels = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    processPrototypes = EReference(ordered=True, unique=True,
                                   containment=True, derived=False, upper=-1)
    sections = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    activations = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    events = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    typeDefinitions = EReference(ordered=True, unique=True,
                                 containment=True, derived=False, upper=-1)
    customEntities = EReference(ordered=True, unique=True,
                                containment=True, derived=False, upper=-1)
    processChains = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    modes = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    modeLabels = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, isrs=None, tasks=None, runnables=None, labels=None, channels=None, processPrototypes=None, sections=None, activations=None, events=None, typeDefinitions=None, customEntities=None, processChains=None, modes=None, modeLabels=None, **kwargs):

        super().__init__(**kwargs)

        if isrs:
            self.isrs.extend(isrs)

        if tasks:
            self.tasks.extend(tasks)

        if runnables:
            self.runnables.extend(runnables)

        if labels:
            self.labels.extend(labels)

        if channels:
            self.channels.extend(channels)

        if processPrototypes:
            self.processPrototypes.extend(processPrototypes)

        if sections:
            self.sections.extend(sections)

        if activations:
            self.activations.extend(activations)

        if events:
            self.events.extend(events)

        if typeDefinitions:
            self.typeDefinitions.extend(typeDefinitions)

        if customEntities:
            self.customEntities.extend(customEntities)

        if processChains:
            self.processChains.extend(processChains)

        if modes:
            self.modes.extend(modes)

        if modeLabels:
            self.modeLabels.extend(modeLabels)

    def modeLiteral(self, mode=None, literal=None):

        raise NotImplementedError('operation modeLiteral(...) not yet implemented')


@abstract
class ActivityGraphItem(BaseObject):
    """An abstract item of a ActivityGraph."""
    _containingExecutable = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='containingExecutable', transient=True)
    _containingProcess = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='containingProcess', transient=True)
    _containingRunnable = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='containingRunnable', transient=True)
    _containingActivityGraph = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='containingActivityGraph', transient=True)

    @property
    def containingExecutable(self):
        raise NotImplementedError('Missing implementation for containingExecutable')

    @property
    def containingProcess(self):
        raise NotImplementedError('Missing implementation for containingProcess')

    @property
    def containingRunnable(self):
        raise NotImplementedError('Missing implementation for containingRunnable')

    @property
    def containingActivityGraph(self):
        raise NotImplementedError('Missing implementation for containingActivityGraph')

    def __init__(self, *, containingExecutable=None, containingProcess=None, containingRunnable=None, containingActivityGraph=None, **kwargs):

        super().__init__(**kwargs)

        if containingExecutable is not None:
            self.containingExecutable = containingExecutable

        if containingProcess is not None:
            self.containingProcess = containingProcess

        if containingRunnable is not None:
            self.containingRunnable = containingRunnable

        if containingActivityGraph is not None:
            self.containingActivityGraph = containingActivityGraph


class Counter(BaseObject):
    """A counter for the call sequence items"""
    prescaler = EAttribute(eType=PositiveLong, unique=False, derived=False,
                           changeable=True, default_value='1')
    offset = EAttribute(eType=NonNegativeLong, unique=False,
                        derived=False, changeable=True, default_value='0')

    def __init__(self, *, prescaler=None, offset=None, **kwargs):

        super().__init__(**kwargs)

        if prescaler is not None:
            self.prescaler = prescaler

        if offset is not None:
            self.offset = offset


class EventMask(BaseObject):
    """A event mask"""
    events = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, events=None, **kwargs):

        super().__init__(**kwargs)

        if events:
            self.events.extend(events)


class ChainedProcessPrototype(BaseObject):

    apply = EAttribute(eType=EInt, unique=False, derived=False, changeable=True, default_value='0')
    offset = EAttribute(eType=EInt, unique=False, derived=False, changeable=True, default_value='0')
    prototype = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, prototype=None, apply=None, offset=None, **kwargs):

        super().__init__(**kwargs)

        if apply is not None:
            self.apply = apply

        if offset is not None:
            self.offset = offset

        if prototype is not None:
            self.prototype = prototype


@abstract
class GeneralPrecedence(BaseObject):
    """General abstraction for precedence"""
    origin = EReference(ordered=True, unique=True, containment=False, derived=False)
    target = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, origin=None, target=None, **kwargs):

        super().__init__(**kwargs)

        if origin is not None:
            self.origin = origin

        if target is not None:
            self.target = target


class DataDependency(BaseObject):

    labels = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    parameters = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    callArguments = EReference(ordered=True, unique=True,
                               containment=False, derived=False, upper=-1)
    _containingRunnable = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='containingRunnable', transient=True)

    @property
    def containingRunnable(self):
        raise NotImplementedError('Missing implementation for containingRunnable')

    def __init__(self, *, labels=None, parameters=None, callArguments=None, containingRunnable=None, **kwargs):

        super().__init__(**kwargs)

        if labels:
            self.labels.extend(labels)

        if parameters:
            self.parameters.extend(parameters)

        if callArguments:
            self.callArguments.extend(callArguments)

        if containingRunnable is not None:
            self.containingRunnable = containingRunnable


class Alias(BaseObject):

    target = EAttribute(eType=EString, unique=False, derived=False, changeable=True)
    alias = EAttribute(eType=EString, unique=False, derived=False, changeable=True)

    def __init__(self, *, target=None, alias=None, **kwargs):

        super().__init__(**kwargs)

        if target is not None:
            self.target = target

        if alias is not None:
            self.alias = alias


class LabelAccessStatistic(BaseObject):
    """Contains information about access statistic values"""
    value = EReference(ordered=True, unique=True, containment=True, derived=False)
    cacheMisses = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, value=None, cacheMisses=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

        if cacheMisses is not None:
            self.cacheMisses = cacheMisses


class RunEntityCallStatistic(BaseObject):

    statistic = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, statistic=None, **kwargs):

        super().__init__(**kwargs)

        if statistic is not None:
            self.statistic = statistic


@abstract
class ReferableBaseObject(IAnnotatable, IReferable):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DerivedMemberobjects(EDerivedCollection):
    pass


class Namespace(ReferableObject):

    nextSegments = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    previousSegment = EReference(ordered=True, unique=True, containment=False, derived=False)
    memberObjects = EReference(ordered=True, unique=True, containment=False,
                               derived=True, upper=-1, transient=True, derived_class=DerivedMemberobjects)

    def __init__(self, *, nextSegments=None, previousSegment=None, memberObjects=None, **kwargs):

        super().__init__(**kwargs)

        if nextSegments:
            self.nextSegments.extend(nextSegments)

        if previousSegment is not None:
            self.previousSegment = previousSegment

        if memberObjects:
            self.memberObjects.extend(memberObjects)

    def getNamePrefixSegments(self):

        raise NotImplementedError('operation getNamePrefixSegments(...) not yet implemented')


class Time(Quantity, Value, TimeComparable):
    """General time class to define time value and unit."""
    value = EAttribute(eType=EBigInteger, unique=False, derived=False,
                       changeable=True, default_value='0')
    unit = EAttribute(eType=TimeUnit, unique=False, derived=False, changeable=True)

    def __init__(self, *, value=None, unit=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

        if unit is not None:
            self.unit = unit

    def toString(self):

        raise NotImplementedError('operation toString(...) not yet implemented')

    def compareTo(self, t=None):

        raise NotImplementedError('operation compareTo(...) not yet implemented')

    def adjustUnit(self):

        raise NotImplementedError('operation adjustUnit(...) not yet implemented')

    def add(self, t=None):

        raise NotImplementedError('operation add(...) not yet implemented')

    def subtract(self, t=None):

        raise NotImplementedError('operation subtract(...) not yet implemented')

    def multiply(self, v=None):

        raise NotImplementedError('operation multiply(...) not yet implemented')

    def multiply(self, v=None):

        raise NotImplementedError('operation multiply(...) not yet implemented')

    def divide(self, t=None):

        raise NotImplementedError('operation divide(...) not yet implemented')


class TimeBoundaries(BoundedTimeDistribution):
    """Defines the upper and lower bounds of a value interval without defining the distribution"""
    samplingType = EAttribute(eType=SamplingType, unique=False, derived=False, changeable=True)

    def __init__(self, *, samplingType=None, **kwargs):

        super().__init__(**kwargs)

        if samplingType is not None:
            self.samplingType = samplingType


class TimeStatistics(BoundedTimeDistribution):
    """Defines the upper bound, lower bound and mean of a value interval without defining the distribution"""
    average = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, average=None, **kwargs):

        super().__init__(**kwargs)

        if average is not None:
            self.average = average


class TimeUniformDistribution(BoundedTimeDistribution):
    """Uniform distribution"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class TimeWeibullEstimatorsDistribution(BoundedTimeDistribution):
    """Weibull Distribution
The parameter of a Weibull distribution (kappa, lambda...) are calculated from the estimators minimum, maximum and average."""
    pRemainPromille = EAttribute(eType=PositiveDouble, unique=False,
                                 derived=False, changeable=True, default_value='1.0')
    average = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, average=None, pRemainPromille=None, **kwargs):

        super().__init__(**kwargs)

        if pRemainPromille is not None:
            self.pRemainPromille = pRemainPromille

        if average is not None:
            self.average = average


class TimeBetaDistribution(BoundedTimeDistribution):
    """Beta distribution"""
    alpha = EAttribute(eType=PositiveDouble, unique=False, derived=False,
                       changeable=True, default_value='1.0')
    beta = EAttribute(eType=PositiveDouble, unique=False, derived=False,
                      changeable=True, default_value='1.0')

    def __init__(self, *, alpha=None, beta=None, **kwargs):

        super().__init__(**kwargs)

        if alpha is not None:
            self.alpha = alpha

        if beta is not None:
            self.beta = beta

    def getAverage(self):

        raise NotImplementedError('operation getAverage(...) not yet implemented')


class DiscreteValueBoundaries(BoundedDiscreteValueDistribution):
    """Defines the upper and lower bounds of a value interval without defining the distribution"""
    samplingType = EAttribute(eType=SamplingType, unique=False, derived=False, changeable=True)

    def __init__(self, *, samplingType=None, **kwargs):

        super().__init__(**kwargs)

        if samplingType is not None:
            self.samplingType = samplingType


class DiscreteValueStatistics(BoundedDiscreteValueDistribution):
    """Defines the upper bound, lower bound and mean of a value interval without defining the distribution"""
    average = EAttribute(eType=EDoubleObject, unique=False, derived=False,
                         changeable=True, default_value='0.0')

    def __init__(self, *, average=None, **kwargs):

        super().__init__(**kwargs)

        if average is not None:
            self.average = average


class DiscreteValueUniformDistribution(BoundedDiscreteValueDistribution):
    """Uniform distribution"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DiscreteValueWeibullEstimatorsDistribution(BoundedDiscreteValueDistribution):
    """Weibull Distribution
The parameter of a Weibull distribution (kappa, lambda...) are calculated from the estimators minimum, maximum and average."""
    average = EAttribute(eType=EDoubleObject, unique=False, derived=False,
                         changeable=True, default_value='0.0')
    pRemainPromille = EAttribute(eType=PositiveDouble, unique=False,
                                 derived=False, changeable=True, default_value='1.0')

    def __init__(self, *, average=None, pRemainPromille=None, **kwargs):

        super().__init__(**kwargs)

        if average is not None:
            self.average = average

        if pRemainPromille is not None:
            self.pRemainPromille = pRemainPromille


class DiscreteValueBetaDistribution(BoundedDiscreteValueDistribution):
    """Beta distribution"""
    alpha = EAttribute(eType=PositiveDouble, unique=False, derived=False,
                       changeable=True, default_value='1.0')
    beta = EAttribute(eType=PositiveDouble, unique=False, derived=False,
                      changeable=True, default_value='1.0')

    def __init__(self, *, alpha=None, beta=None, **kwargs):

        super().__init__(**kwargs)

        if alpha is not None:
            self.alpha = alpha

        if beta is not None:
            self.beta = beta

    def getAverage(self):

        raise NotImplementedError('operation getAverage(...) not yet implemented')


class ContinuousValueBoundaries(BoundedContinuousValueDistribution):
    """Defines the upper and lower bounds of a value interval without defining the distribution"""
    samplingType = EAttribute(eType=SamplingType, unique=False, derived=False, changeable=True)

    def __init__(self, *, samplingType=None, **kwargs):

        super().__init__(**kwargs)

        if samplingType is not None:
            self.samplingType = samplingType


class ContinuousValueStatistics(BoundedContinuousValueDistribution):
    """Defines the upper bound, lower bound and mean of a value interval without defining the distribution"""
    average = EAttribute(eType=EDoubleObject, unique=False, derived=False,
                         changeable=True, default_value='0.0')

    def __init__(self, *, average=None, **kwargs):

        super().__init__(**kwargs)

        if average is not None:
            self.average = average


class ContinuousValueUniformDistribution(BoundedContinuousValueDistribution):
    """Uniform distribution"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ContinuousValueWeibullEstimatorsDistribution(BoundedContinuousValueDistribution):
    """Weibull Distribution
The parameter of a Weibull distribution (kappa, lambda...) are calculated from the estimators minimum, maximum and average."""
    average = EAttribute(eType=EDoubleObject, unique=False, derived=False,
                         changeable=True, default_value='0.0')
    pRemainPromille = EAttribute(eType=PositiveDouble, unique=False,
                                 derived=False, changeable=True, default_value='1.0')

    def __init__(self, *, average=None, pRemainPromille=None, **kwargs):

        super().__init__(**kwargs)

        if average is not None:
            self.average = average

        if pRemainPromille is not None:
            self.pRemainPromille = pRemainPromille


class ContinuousValueBetaDistribution(BoundedContinuousValueDistribution):
    """Beta distribution"""
    alpha = EAttribute(eType=PositiveDouble, unique=False, derived=False,
                       changeable=True, default_value='1.0')
    beta = EAttribute(eType=PositiveDouble, unique=False, derived=False,
                      changeable=True, default_value='1.0')

    def __init__(self, *, alpha=None, beta=None, **kwargs):

        super().__init__(**kwargs)

        if alpha is not None:
            self.alpha = alpha

        if beta is not None:
            self.beta = beta

    def getAverage(self):

        raise NotImplementedError('operation getAverage(...) not yet implemented')


class DerivedMemberobjects(EDerivedCollection):
    pass


class ComponentStructure(ReferableObject):

    structureType = EAttribute(eType=EString, unique=False, derived=False, changeable=True)
    subStructures = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    memberObjects = EReference(ordered=True, unique=True, containment=False,
                               derived=True, upper=-1, transient=True, derived_class=DerivedMemberobjects)

    def __init__(self, *, structureType=None, subStructures=None, memberObjects=None, **kwargs):

        super().__init__(**kwargs)

        if structureType is not None:
            self.structureType = structureType

        if subStructures:
            self.subStructures.extend(subStructures)

        if memberObjects:
            self.memberObjects.extend(memberObjects)

    def getContainingStructure(self):

        raise NotImplementedError('operation getContainingStructure(...) not yet implemented')

    def getDefaultNameSeparator(self):

        raise NotImplementedError('operation getDefaultNameSeparator(...) not yet implemented')

    def getNamePrefixSegments(self):

        raise NotImplementedError('operation getNamePrefixSegments(...) not yet implemented')


class EventConfig(BaseObject, INamed):

    event = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, event=None, **kwargs):

        super().__init__(**kwargs)

        if event is not None:
            self.event = event


class TargetMemory(DataConstraintTarget, BaseObject):
    """A memory target description
A memory can be a target for data-constraints
memories: the reference to zero or more Memories. If this list is empty, the target stands for all memories!"""
    memories = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, memories=None, **kwargs):

        super().__init__(**kwargs)

        if memories:
            self.memories.extend(memories)


class LabelEntityGroup(LabelGroup, BaseObject):
    """A group of labels that can be paired or separated by a data-constraint"""
    labels = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, labels=None, **kwargs):

        super().__init__(**kwargs)

        if labels:
            self.labels.extend(labels)


class RunnableEntityGroup(RunnableGroup, BaseObject):
    """A group of runnables that can be paired or separated by a runnable-constraint"""
    runnables = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, runnables=None, **kwargs):

        super().__init__(**kwargs)

        if runnables:
            self.runnables.extend(runnables)


class ProcessEntityGroup(ProcessGroup, BaseObject):
    """A group of processes that can be paired or separated by a process-constraint"""
    processes = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, processes=None, **kwargs):

        super().__init__(**kwargs)

        if processes:
            self.processes.extend(processes)


@abstract
class AbstractEventChain(BaseObject, INamed):
    """Describes an event chain which must have a minimum of two events (stimulus and response)
If there are more events the event chain have to be divided into segments. Each segment is another event chain.
Alternative event paths are contained in strands.
stimulus: Beginning of chain
response: End of chain
segments: Sub event chains
strands: alternative event paths"""
    itemType = EAttribute(eType=EventChainItemType, unique=False, derived=False, changeable=True)
    minItemsCompleted = EAttribute(eType=PositiveInt, unique=False,
                                   derived=False, changeable=True, default_value='1')
    stimulus = EReference(ordered=True, unique=True, containment=False, derived=False)
    response = EReference(ordered=True, unique=True, containment=False, derived=False)
    items = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, stimulus=None, response=None, items=None, itemType=None, minItemsCompleted=None, **kwargs):

        super().__init__(**kwargs)

        if itemType is not None:
            self.itemType = itemType

        if minItemsCompleted is not None:
            self.minItemsCompleted = minItemsCompleted

        if stimulus is not None:
            self.stimulus = stimulus

        if response is not None:
            self.response = response

        if items:
            self.items.extend(items)


class EventChainReference(BaseObject, EventChainItem):

    eventChain = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, eventChain=None, **kwargs):

        super().__init__(**kwargs)

        if eventChain is not None:
            self.eventChain = eventChain


class EventChainContainer(BaseObject, EventChainItem):

    eventChain = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, eventChain=None, **kwargs):

        super().__init__(**kwargs)

        if eventChain is not None:
            self.eventChain = eventChain


@abstract
class Requirement(BaseObject, INamed):

    severity = EAttribute(eType=Severity, unique=False, derived=False, changeable=True)
    limit = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, severity=None, limit=None, **kwargs):

        super().__init__(**kwargs)

        if severity is not None:
            self.severity = severity

        if limit is not None:
            self.limit = limit


class TaskAllocation(BaseObject, ISchedulingParameterContainer):

    task = EReference(ordered=True, unique=True, containment=False, derived=False)
    scheduler = EReference(ordered=True, unique=True, containment=False, derived=False)
    affinity = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, task=None, scheduler=None, affinity=None, **kwargs):

        super().__init__(**kwargs)

        if task is not None:
            self.task = task

        if scheduler is not None:
            self.scheduler = scheduler

        if affinity:
            self.affinity.extend(affinity)


class OperatingSystem(BaseObject, INamed):

    overhead = EReference(ordered=True, unique=True, containment=False, derived=False)
    taskSchedulers = EReference(ordered=True, unique=True,
                                containment=True, derived=False, upper=-1)
    interruptControllers = EReference(ordered=True, unique=True,
                                      containment=True, derived=False, upper=-1)
    osDataConsistency = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, overhead=None, taskSchedulers=None, interruptControllers=None, osDataConsistency=None, **kwargs):

        super().__init__(**kwargs)

        if overhead is not None:
            self.overhead = overhead

        if taskSchedulers:
            self.taskSchedulers.extend(taskSchedulers)

        if interruptControllers:
            self.interruptControllers.extend(interruptControllers)

        if osDataConsistency is not None:
            self.osDataConsistency = osDataConsistency


class ProcessAllocationConstraint(CoreAllocationConstraint):
    """ProcessAllocationConstraints describe the constraints for
Process-to-Core allocations"""
    process = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, process=None, **kwargs):

        super().__init__(**kwargs)

        if process is not None:
            self.process = process


class ProcessPrototypeAllocationConstraint(CoreAllocationConstraint):
    """ProcessPrototypeAllocationConstraints describe the constraints for
ProcessPrototype-to-Core allocations"""
    processPrototype = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, processPrototype=None, **kwargs):

        super().__init__(**kwargs)

        if processPrototype is not None:
            self.processPrototype = processPrototype


class RunnableAllocationConstraint(CoreAllocationConstraint):
    """RunnableAllocationConstraints describe the constraints for
Runnable-to-Core allocations"""
    runnable = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, runnable=None, **kwargs):

        super().__init__(**kwargs)

        if runnable is not None:
            self.runnable = runnable


class AbstractElementMappingConstraint(MemoryMappingConstraint):
    """AbstractElementMappingConstraints describe the constraints for
AbstractMemoryElement-to-Memory Mapping"""
    abstractElement = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, abstractElement=None, **kwargs):

        super().__init__(**kwargs)

        if abstractElement is not None:
            self.abstractElement = abstractElement


class CoreClassification(Classification):

    classifiers = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, classifiers=None, **kwargs):

        super().__init__(**kwargs)

        if classifiers:
            self.classifiers.extend(classifiers)


class MemoryClassification(Classification):

    classifiers = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, classifiers=None, **kwargs):

        super().__init__(**kwargs)

        if classifiers:
            self.classifiers.extend(classifiers)


class ModeAssignment(ModeValue):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ModeConditionDisjunction(BaseObject, ISatisfiable):

    entries = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, entries=None, **kwargs):

        super().__init__(**kwargs)

        if entries:
            self.entries.extend(entries)

    def isSatisfiedBy(self, context=None):

        raise NotImplementedError('operation isSatisfiedBy(...) not yet implemented')


class ConditionConjunction(BaseObject, ConditionDisjunctionEntry):

    entries = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, entries=None, **kwargs):

        super().__init__(**kwargs)

        if entries:
            self.entries.extend(entries)


class ActivityGraph(BaseObject, IActivityGraphItemContainer):
    """Describes the different execution paths of a process or runnable"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ModeSwitch(ActivityGraphItem):
    """A switch in the ActivityGraph, the selected path depends on the value of the provided mode conditions.

@deprecated Use more general Switch instead."""
    entries = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    defaultEntry = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, entries=None, defaultEntry=None, **kwargs):

        super().__init__(**kwargs)

        if entries:
            self.entries.extend(entries)

        if defaultEntry is not None:
            self.defaultEntry = defaultEntry


class ModeSwitchDefault(BaseObject, IActivityGraphItemContainer):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Switch(ActivityGraphItem):
    """A switch in the ActivityGraph, the selected path depends on the value of the provided mode conditions.

@since 2.0"""
    entries = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    defaultEntry = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, entries=None, defaultEntry=None, **kwargs):

        super().__init__(**kwargs)

        if entries:
            self.entries.extend(entries)

        if defaultEntry is not None:
            self.defaultEntry = defaultEntry


class SwitchDefault(BaseObject, IActivityGraphItemContainer):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ProbabilitySwitch(ActivityGraphItem):
    """A switch in the ActivityGraph, each path has a probability."""
    entries = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, entries=None, **kwargs):

        super().__init__(**kwargs)

        if entries:
            self.entries.extend(entries)


class ProbabilitySwitchEntry(BaseObject, IActivityGraphItemContainer):
    """A switch entry for a ProbabilitySwitch.
It describes a path of the switch and it's probability."""
    probability = EAttribute(eType=EDouble, unique=False, derived=False,
                             changeable=True, default_value='0.0')

    def __init__(self, *, probability=None, **kwargs):

        super().__init__(**kwargs)

        if probability is not None:
            self.probability = probability


class WaitEvent(ActivityGraphItem):
    """Let the process wait for a combination of events defined by eventMask
maskType defines if the events in eventMask are linked by a AND or OR"""
    maskType = EAttribute(eType=WaitEventType, unique=False, derived=False, changeable=True)
    waitingBehaviour = EAttribute(eType=WaitingBehaviour, unique=False,
                                  derived=False, changeable=True)
    eventMask = EReference(ordered=True, unique=True, containment=True, derived=False)
    counter = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, eventMask=None, maskType=None, waitingBehaviour=None, counter=None, **kwargs):

        super().__init__(**kwargs)

        if maskType is not None:
            self.maskType = maskType

        if waitingBehaviour is not None:
            self.waitingBehaviour = waitingBehaviour

        if eventMask is not None:
            self.eventMask = eventMask

        if counter is not None:
            self.counter = counter


class SetEvent(ActivityGraphItem):
    """Sets the events of eventMask
These events can be set for a specific process, if there is no process, is is global (for all processes)
If there is a process, it is possible to set the event for a specific process instance that is currently activated"""
    eventMask = EReference(ordered=True, unique=True, containment=True, derived=False)
    process = EReference(ordered=True, unique=True, containment=False, derived=False)
    counter = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, eventMask=None, process=None, counter=None, **kwargs):

        super().__init__(**kwargs)

        if eventMask is not None:
            self.eventMask = eventMask

        if process is not None:
            self.process = process

        if counter is not None:
            self.counter = counter


class ClearEvent(ActivityGraphItem):
    """Clears the events of eventMask"""
    eventMask = EReference(ordered=True, unique=True, containment=True, derived=False)
    counter = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, eventMask=None, counter=None, **kwargs):

        super().__init__(**kwargs)

        if eventMask is not None:
            self.eventMask = eventMask

        if counter is not None:
            self.counter = counter


class InterProcessTrigger(ActivityGraphItem):
    """Triggers a stimulus to activate its processes"""
    stimulus = EReference(ordered=True, unique=True, containment=False, derived=False)
    counter = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, stimulus=None, counter=None, **kwargs):

        super().__init__(**kwargs)

        if stimulus is not None:
            self.stimulus = stimulus

        if counter is not None:
            self.counter = counter


class EnforcedMigration(ActivityGraphItem):
    """Migrates task to core of resource owner"""
    resourceOwner = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, resourceOwner=None, **kwargs):

        super().__init__(**kwargs)

        if resourceOwner is not None:
            self.resourceOwner = resourceOwner


class SchedulePoint(ActivityGraphItem):
    """Triggers scheduler"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class TerminateProcess(ActivityGraphItem):
    """Terminates the process"""
    counter = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, counter=None, **kwargs):

        super().__init__(**kwargs)

        if counter is not None:
            self.counter = counter


class AccessPrecedenceSpec(GeneralPrecedence):

    orderType = EAttribute(eType=AccessPrecedenceType, unique=False, derived=False, changeable=True)
    label = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, label=None, orderType=None, **kwargs):

        super().__init__(**kwargs)

        if orderType is not None:
            self.orderType = orderType

        if label is not None:
            self.label = label


class OrderPrecedenceSpec(GeneralPrecedence):

    orderType = EAttribute(eType=OrderType, unique=False, derived=False, changeable=True)

    def __init__(self, *, orderType=None, **kwargs):

        super().__init__(**kwargs)

        if orderType is not None:
            self.orderType = orderType


@abstract
class ComputationItem(ActivityGraphItem):
    """Representation of a object that describes computation"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ExecutionNeed(ActivityGraphItem):
    """Representation of the execution needs of a Runnable (default and core-specific)"""
    needs = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, needs=None, **kwargs):

        super().__init__(**kwargs)

        if needs:
            self.needs.extend(needs)


class ModeLabelAccess(ActivityGraphItem):
    """Representation of a mode label access of a run entity."""
    access = EAttribute(eType=ModeLabelAccessEnum, unique=False, derived=False, changeable=True)
    value = EAttribute(eType=EString, unique=False, derived=False, changeable=True)
    step = EAttribute(eType=PositiveInt, unique=False, derived=False,
                      changeable=True, default_value='1')
    data = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, data=None, access=None, value=None, step=None, **kwargs):

        super().__init__(**kwargs)

        if access is not None:
            self.access = access

        if value is not None:
            self.value = value

        if step is not None:
            self.step = step

        if data is not None:
            self.data = data

    def validateInvariants(self, diagnostics=None, context=None):

        raise NotImplementedError('operation validateInvariants(...) not yet implemented')


@abstract
class ChannelAccess(ActivityGraphItem):

    elements = EAttribute(eType=EInt, unique=False, derived=False,
                          changeable=True, default_value='0')
    data = EReference(ordered=True, unique=True, containment=False, derived=False)
    transmissionPolicy = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, data=None, elements=None, transmissionPolicy=None, **kwargs):

        super().__init__(**kwargs)

        if elements is not None:
            self.elements = elements

        if data is not None:
            self.data = data

        if transmissionPolicy is not None:
            self.transmissionPolicy = transmissionPolicy


class SemaphoreAccess(ActivityGraphItem):
    """Describes an semaphore access"""
    access = EAttribute(eType=SemaphoreAccessEnum, unique=False, derived=False, changeable=True)
    waitingBehaviour = EAttribute(eType=WaitingBehaviour, unique=False,
                                  derived=False, changeable=True)
    semaphore = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, semaphore=None, access=None, waitingBehaviour=None, **kwargs):

        super().__init__(**kwargs)

        if access is not None:
            self.access = access

        if waitingBehaviour is not None:
            self.waitingBehaviour = waitingBehaviour

        if semaphore is not None:
            self.semaphore = semaphore


@abstract
class SenderReceiverCommunication(ActivityGraphItem):
    """An abstract description for sender-receiver-communication (it can be read or write)"""
    buffered = EAttribute(eType=EBoolean, unique=False, derived=False,
                          changeable=True, default_value='false')
    label = EReference(ordered=True, unique=True, containment=False, derived=False)
    port = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, buffered=None, label=None, port=None, **kwargs):

        super().__init__(**kwargs)

        if buffered is not None:
            self.buffered = buffered

        if label is not None:
            self.label = label

        if port is not None:
            self.port = port


@abstract
class ServerCall(ActivityGraphItem):
    """An abstract description for client/server communication
It refers to a required runnable that describes the called server operation"""
    serverRunnable = EReference(ordered=True, unique=True, containment=False, derived=False)
    port = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, serverRunnable=None, port=None, **kwargs):

        super().__init__(**kwargs)

        if serverRunnable is not None:
            self.serverRunnable = serverRunnable

        if port is not None:
            self.port = port


class CustomEventTrigger(ActivityGraphItem):
    """Explicitly trigger a custom event from a runnable."""
    event = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, event=None, **kwargs):

        super().__init__(**kwargs)

        if event is not None:
            self.event = event


@abstract
class CompoundType(BaseObject, DataType):
    """Couple of compound data types"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class TypeRef(BaseObject, DataType):

    typeDef = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, typeDef=None, **kwargs):

        super().__init__(**kwargs)

        if typeDef is not None:
            self.typeDef = typeDef


class ModeLabelAssignment(ActivityGraphItem):

    globalLabel = EReference(ordered=True, unique=True, containment=False, derived=False)
    localLabel = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, globalLabel=None, localLabel=None, **kwargs):

        super().__init__(**kwargs)

        if globalLabel is not None:
            self.globalLabel = globalLabel

        if localLabel is not None:
            self.localLabel = localLabel

    def validateInvariants(self, diagnostics=None, context=None):

        raise NotImplementedError('operation validateInvariants(...) not yet implemented')


@abstract
class Mode(ReferableBaseObject):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ModeLiteral(ReferableBaseObject):

    containingMode = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, containingMode=None, **kwargs):

        super().__init__(**kwargs)

        if containingMode is not None:
            self.containingMode = containingMode

    def getNamePrefixSegments(self):

        raise NotImplementedError('operation getNamePrefixSegments(...) not yet implemented')

    def toString(self):

        raise NotImplementedError('operation toString(...) not yet implemented')


class ComponentsModel(BaseObject, IComponentContainer, IInterfaceContainer):

    structures = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    systems = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, structures=None, systems=None, **kwargs):

        super().__init__(**kwargs)

        if structures:
            self.structures.extend(structures)

        if systems:
            self.systems.extend(systems)


class Connector(BaseObject, INamed, ITaggable):

    containingSystem = EReference(ordered=True, unique=True, containment=False, derived=False)
    sourcePort = EReference(ordered=True, unique=True, containment=True, derived=False)
    targetPort = EReference(ordered=True, unique=True, containment=True, derived=False)
    implementedInterfaces = EReference(ordered=True, unique=True,
                                       containment=True, derived=False, upper=-1)

    def __init__(self, *, containingSystem=None, sourcePort=None, targetPort=None, implementedInterfaces=None, **kwargs):

        super().__init__(**kwargs)

        if containingSystem is not None:
            self.containingSystem = containingSystem

        if sourcePort is not None:
            self.sourcePort = sourcePort

        if targetPort is not None:
            self.targetPort = targetPort

        if implementedInterfaces:
            self.implementedInterfaces.extend(implementedInterfaces)


class RunnableSequencingConstraint(ReferableBaseObject):

    orderType = EAttribute(eType=RunnableOrderType, unique=False, derived=False, changeable=True)
    runnableGroups = EReference(ordered=True, unique=True,
                                containment=True, derived=False, upper=-1)
    processScope = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, orderType=None, runnableGroups=None, processScope=None, **kwargs):

        super().__init__(**kwargs)

        if orderType is not None:
            self.orderType = orderType

        if runnableGroups:
            self.runnableGroups.extend(runnableGroups)

        if processScope:
            self.processScope.extend(processScope)


@abstract
class AffinityConstraint(ReferableBaseObject):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class TargetCore(RunnableConstraintTarget, ProcessConstraintTarget, BaseObject):
    """A core target description
A core can be a target for runnable-constraints, process-constraints and scheduler-constraints
cores: the reference to zero or more Cores. If this list is empty, the target stands for all cores!"""
    cores = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, cores=None, **kwargs):

        super().__init__(**kwargs)

        if cores:
            self.cores.extend(cores)


class TargetScheduler(RunnableConstraintTarget, ProcessConstraintTarget, BaseObject):
    """A scheduler target description
A scheduler can be a target for runnable-constraints and process-constraints
schedulers: the reference to zero or more Schedulers. If this list is empty, the target stands for all schedulers!"""
    schedulers = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, schedulers=None, **kwargs):

        super().__init__(**kwargs)

        if schedulers:
            self.schedulers.extend(schedulers)


class TagGroup(RunnableGroup, ProcessGroup, BaseObject):
    """A group that contains only a tag and groups all objects that are marked with this tag
This can be runnables or processes"""
    tag = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, tag=None, **kwargs):

        super().__init__(**kwargs)

        if tag is not None:
            self.tag = tag


class SubEventChain(AbstractEventChain):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class TimingConstraint(ReferableBaseObject):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class PhysicalSectionConstraint(ReferableBaseObject):
    """This contraints is used to limit a section in Memories"""
    section = EReference(ordered=True, unique=True, containment=False, derived=False)
    memories = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, section=None, memories=None, **kwargs):

        super().__init__(**kwargs)

        if section is not None:
            self.section = section

        if memories:
            self.memories.extend(memories)


class DataAgeConstraint(ReferableBaseObject):

    runnable = EReference(ordered=True, unique=True, containment=False, derived=False)
    label = EReference(ordered=True, unique=True, containment=False, derived=False)
    dataAge = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, runnable=None, label=None, dataAge=None, **kwargs):

        super().__init__(**kwargs)

        if runnable is not None:
            self.runnable = runnable

        if label is not None:
            self.label = label

        if dataAge is not None:
            self.dataAge = dataAge


class ProcessRequirement(Requirement):

    process = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, process=None, **kwargs):

        super().__init__(**kwargs)

        if process is not None:
            self.process = process


class RunnableRequirement(Requirement):

    runnable = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, runnable=None, **kwargs):

        super().__init__(**kwargs)

        if runnable is not None:
            self.runnable = runnable


class ArchitectureRequirement(Requirement):

    component = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, component=None, **kwargs):

        super().__init__(**kwargs)

        if component is not None:
            self.component = component


class ProcessChainRequirement(Requirement):

    processChain = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, processChain=None, **kwargs):

        super().__init__(**kwargs)

        if processChain is not None:
            self.processChain = processChain


class DataCoherencyGroup(ReferableBaseObject):

    direction = EAttribute(eType=CoherencyDirection, unique=False, derived=False, changeable=True)
    labels = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    scope = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, labels=None, scope=None, direction=None, **kwargs):

        super().__init__(**kwargs)

        if direction is not None:
            self.direction = direction

        if labels:
            self.labels.extend(labels)

        if scope is not None:
            self.scope = scope


class DataStabilityGroup(ReferableBaseObject):

    labels = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    scope = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, labels=None, scope=None, **kwargs):

        super().__init__(**kwargs)

        if labels:
            self.labels.extend(labels)

        if scope is not None:
            self.scope = scope


class HwFeature(ReferableBaseObject):

    value = EAttribute(eType=EDouble, unique=False, derived=False,
                       changeable=True, default_value='0.0')
    containingCategory = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, containingCategory=None, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

        if containingCategory is not None:
            self.containingCategory = containingCategory

    def getNamePrefixSegments(self):

        raise NotImplementedError('operation getNamePrefixSegments(...) not yet implemented')

    def toString(self):

        raise NotImplementedError('operation toString(...) not yet implemented')


class PhysicalSectionMapping(ReferableBaseObject):

    startAddress = EAttribute(eType=Address, unique=False, derived=False,
                              changeable=True, default_value='0')
    endAddress = EAttribute(eType=Address, unique=False, derived=False,
                            changeable=True, default_value='0')
    origin = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    memory = EReference(ordered=True, unique=True, containment=False, derived=False)
    labels = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    runEntities = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, origin=None, memory=None, startAddress=None, endAddress=None, labels=None, runEntities=None, **kwargs):

        super().__init__(**kwargs)

        if startAddress is not None:
            self.startAddress = startAddress

        if endAddress is not None:
            self.endAddress = endAddress

        if origin:
            self.origin.extend(origin)

        if memory is not None:
            self.memory = memory

        if labels:
            self.labels.extend(labels)

        if runEntities:
            self.runEntities.extend(runEntities)


class DerivedSemaphoreaccesses(EDerivedCollection):
    pass


class DerivedReferringcomponents(EDerivedCollection):
    pass


class Semaphore(ReferableBaseObject):
    """name: Name of semaphore
maxValue: maximum number of users which can access the semaphore simultaneously
initialValue: number of users which access semaphore at system startup
priorityCeilingProtocol: enables priority ceiling for this resource"""
    semaphoreType = EAttribute(eType=SemaphoreType, unique=False, derived=False, changeable=True)
    initialValue = EAttribute(eType=NonNegativeInt, unique=False,
                              derived=False, changeable=True, default_value='0')
    maxValue = EAttribute(eType=PositiveInt, unique=False, derived=False,
                          changeable=True, default_value='1')
    priorityCeilingProtocol = EAttribute(
        eType=EBoolean, unique=False, derived=False, changeable=True, default_value='false')
    semaphoreAccesses = EReference(ordered=True, unique=True, containment=False,
                                   derived=True, upper=-1, transient=True, derived_class=DerivedSemaphoreaccesses)
    referringComponents = EReference(ordered=True, unique=True, containment=False,
                                     derived=True, upper=-1, transient=True, derived_class=DerivedReferringcomponents)

    def __init__(self, *, semaphoreType=None, initialValue=None, maxValue=None, priorityCeilingProtocol=None, semaphoreAccesses=None, referringComponents=None, **kwargs):

        super().__init__(**kwargs)

        if semaphoreType is not None:
            self.semaphoreType = semaphoreType

        if initialValue is not None:
            self.initialValue = initialValue

        if maxValue is not None:
            self.maxValue = maxValue

        if priorityCeilingProtocol is not None:
            self.priorityCeilingProtocol = priorityCeilingProtocol

        if semaphoreAccesses:
            self.semaphoreAccesses.extend(semaphoreAccesses)

        if referringComponents:
            self.referringComponents.extend(referringComponents)


class VendorOperatingSystem(OperatingSystem):

    osName = EAttribute(eType=EString, unique=False, derived=False, changeable=True)
    vendor = EAttribute(eType=EString, unique=False, derived=False, changeable=True)
    version = EAttribute(eType=EString, unique=False, derived=False, changeable=True)

    def __init__(self, *, osName=None, vendor=None, version=None, **kwargs):

        super().__init__(**kwargs)

        if osName is not None:
            self.osName = osName

        if vendor is not None:
            self.vendor = vendor

        if version is not None:
            self.version = version


class ModeConditionConjunction(BaseObject, ModeConditionDisjunctionEntry):

    entries = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, entries=None, **kwargs):

        super().__init__(**kwargs)

        if entries:
            self.entries.extend(entries)

    def isSatisfiedBy(self, context=None):

        raise NotImplementedError('operation isSatisfiedBy(...) not yet implemented')


@abstract
class ModeCondition(Condition, ModeConditionDisjunctionEntry):

    relation = EAttribute(eType=RelationalOperator, unique=False, derived=False, changeable=True)

    def __init__(self, *, relation=None, **kwargs):

        super().__init__(**kwargs)

        if relation is not None:
            self.relation = relation


class ChannelFillCondition(BaseObject, Condition):

    relation = EAttribute(eType=RelationalOperator, unique=False, derived=False, changeable=True)
    fillLevel = EAttribute(eType=NonNegativeInt, unique=False, derived=False, changeable=True)
    channel = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, channel=None, relation=None, fillLevel=None, **kwargs):

        super().__init__(**kwargs)

        if relation is not None:
            self.relation = relation

        if fillLevel is not None:
            self.fillLevel = fillLevel

        if channel is not None:
            self.channel = channel


@abstract
class Clock(ReferableBaseObject):
    """Within a Scenario a Clock defines the predefined curve progression in a simulation"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ProcessChain(ReferableBaseObject):
    """Groups a list of processes to a process chain.
This does not define how the processes are chained, like being executed by one parent or like they trigger each other
This just defines that the processes should be chained."""
    processes = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, processes=None, **kwargs):

        super().__init__(**kwargs)

        if processes:
            self.processes.extend(processes)


class ModeSwitchEntry(BaseObject, INamed, IActivityGraphItemContainer):
    """A switch entry for a ModeSwitch.
It describes a path of the switch and the required mode condition to use this path."""
    condition = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, condition=None, **kwargs):

        super().__init__(**kwargs)

        if condition is not None:
            self.condition = condition


class SwitchEntry(BaseObject, INamed, IActivityGraphItemContainer):
    """A switch entry for a Switch.
It describes a path of the switch and the required mode condition to use this path."""
    condition = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, condition=None, **kwargs):

        super().__init__(**kwargs)

        if condition is not None:
            self.condition = condition


class WhileLoop(ActivityGraphItem, IActivityGraphItemContainer):
    """A While loop in the ActivityGraph.
The (repeated) execution depends on the value of the provided mode conditions.

@since 1.2"""
    condition = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, condition=None, **kwargs):

        super().__init__(**kwargs)

        if condition is not None:
            self.condition = condition


class DerivedLabels(EDerivedCollection):
    pass


class DerivedRunnables(EDerivedCollection):
    pass


class Section(ReferableBaseObject):
    """A section is a logical structure, which contains labels and abstract run entities.
It is used to provide an easy mechanism to distribute objects to memory,
which are belonging together."""
    asilLevel = EAttribute(eType=ASILType, unique=False, derived=False, changeable=True)
    labels = EReference(ordered=True, unique=True, containment=False, derived=True,
                        upper=-1, transient=True, derived_class=DerivedLabels)
    runnables = EReference(ordered=True, unique=True, containment=False,
                           derived=True, upper=-1, transient=True, derived_class=DerivedRunnables)

    def __init__(self, *, asilLevel=None, labels=None, runnables=None, **kwargs):

        super().__init__(**kwargs)

        if asilLevel is not None:
            self.asilLevel = asilLevel

        if labels:
            self.labels.extend(labels)

        if runnables:
            self.runnables.extend(runnables)


class Ticks(ComputationItem):
    """Representation of the execution IDiscreteValueDeviation of a Runnable (default and core-specific)"""
    default = EReference(ordered=True, unique=True, containment=True, derived=False)
    extended = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, default=None, extended=None, **kwargs):

        super().__init__(**kwargs)

        if default is not None:
            self.default = default

        if extended:
            self.extended.extend(extended)


class ChannelSend(ChannelAccess):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ChannelReceive(ChannelAccess):

    receiveOperation = EAttribute(eType=ReceiveOperation, unique=False,
                                  derived=False, changeable=True)
    dataMustBeNew = EAttribute(eType=EBoolean, unique=False, derived=False,
                               changeable=True, default_value='false')
    elementIndex = EAttribute(eType=EInt, unique=False, derived=False,
                              changeable=True, default_value='0')
    lowerBound = EAttribute(eType=EInt, unique=False, derived=False,
                            changeable=True, default_value='0')

    def __init__(self, *, receiveOperation=None, dataMustBeNew=None, elementIndex=None, lowerBound=None, **kwargs):

        super().__init__(**kwargs)

        if receiveOperation is not None:
            self.receiveOperation = receiveOperation

        if dataMustBeNew is not None:
            self.dataMustBeNew = dataMustBeNew

        if elementIndex is not None:
            self.elementIndex = elementIndex

        if lowerBound is not None:
            self.lowerBound = lowerBound


class SenderReceiverRead(SenderReceiverCommunication):
    """The read operation of the receiver of the sender-receiver-communication"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class SenderReceiverWrite(SenderReceiverCommunication):
    """The write operation of the sender of the sender-receiver-communication
It contains the runnables that have the corresponding SenderReceiverRead"""
    notifiedRunnables = EReference(ordered=True, unique=True,
                                   containment=False, derived=False, upper=-1)

    def __init__(self, *, notifiedRunnables=None, **kwargs):

        super().__init__(**kwargs)

        if notifiedRunnables:
            self.notifiedRunnables.extend(notifiedRunnables)


class SynchronousServerCall(ServerCall):
    """A synchronous server call"""
    waitingBehaviour = EAttribute(eType=WaitingBehaviour, unique=False,
                                  derived=False, changeable=True)

    def __init__(self, *, waitingBehaviour=None, **kwargs):

        super().__init__(**kwargs)

        if waitingBehaviour is not None:
            self.waitingBehaviour = waitingBehaviour


class AsynchronousServerCall(ServerCall):
    """A asynchronous server call
It refers to a optional runnable that exploits the results produced by the server"""
    resultRunnable = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, resultRunnable=None, **kwargs):

        super().__init__(**kwargs)

        if resultRunnable is not None:
            self.resultRunnable = resultRunnable


class GetResultServerCall(ServerCall):
    """Get the result of a previous asynchronous server call"""
    blockingType = EAttribute(eType=BlockingType, unique=False, derived=False, changeable=True)

    def __init__(self, *, blockingType=None, **kwargs):

        super().__init__(**kwargs)

        if blockingType is not None:
            self.blockingType = blockingType


class CallArgument(ReferableObject, IDependsOn):

    containingCall = EReference(ordered=True, unique=True, containment=False, derived=False)
    parameter = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, containingCall=None, parameter=None, **kwargs):

        super().__init__(**kwargs)

        if containingCall is not None:
            self.containingCall = containingCall

        if parameter is not None:
            self.parameter = parameter

    def getName(self):

        raise NotImplementedError('operation getName(...) not yet implemented')

    def getNamePrefixSegments(self):

        raise NotImplementedError('operation getNamePrefixSegments(...) not yet implemented')


class RunnableCall(ActivityGraphItem, ITaggable):
    """Representation of a runnable call of a run entity."""
    runnable = EReference(ordered=True, unique=True, containment=False, derived=False)
    arguments = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    context = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    counter = EReference(ordered=True, unique=True, containment=True, derived=False)
    statistic = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, runnable=None, arguments=None, context=None, counter=None, statistic=None, **kwargs):

        super().__init__(**kwargs)

        if runnable is not None:
            self.runnable = runnable

        if arguments:
            self.arguments.extend(arguments)

        if context:
            self.context.extend(context)

        if counter is not None:
            self.counter = counter

        if statistic is not None:
            self.statistic = statistic


class StructEntry(BaseObject, INamed, ITaggable):
    """Representation of one struct entry"""
    dataType = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, dataType=None, **kwargs):

        super().__init__(**kwargs)

        if dataType is not None:
            self.dataType = dataType


class Array(CompoundType):
    """Representation of an array data type"""
    numberElements = EAttribute(eType=EInt, unique=False, derived=False,
                                changeable=True, default_value='0')
    dataType = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, numberElements=None, dataType=None, **kwargs):

        super().__init__(**kwargs)

        if numberElements is not None:
            self.numberElements = numberElements

        if dataType is not None:
            self.dataType = dataType


class Pointer(CompoundType):
    """Representing a pointer"""
    dataType = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, dataType=None, **kwargs):

        super().__init__(**kwargs)

        if dataType is not None:
            self.dataType = dataType


class LocalModeLabel(ReferableBaseObject):

    defaultValue = EAttribute(eType=EString, unique=False, derived=False, changeable=True)
    containingExecutable = EReference(ordered=True, unique=True, containment=False, derived=False)
    mode = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, containingExecutable=None, mode=None, defaultValue=None, **kwargs):

        super().__init__(**kwargs)

        if defaultValue is not None:
            self.defaultValue = defaultValue

        if containingExecutable is not None:
            self.containingExecutable = containingExecutable

        if mode is not None:
            self.mode = mode

    def getNamePrefixSegments(self):

        raise NotImplementedError('operation getNamePrefixSegments(...) not yet implemented')

    def validateInvariants(self, diagnostics=None, context=None):

        raise NotImplementedError('operation validateInvariants(...) not yet implemented')

    def isEnum(self):

        raise NotImplementedError('operation isEnum(...) not yet implemented')

    def isNumeric(self):

        raise NotImplementedError('operation isNumeric(...) not yet implemented')


class LocalModeLabelAssignment(LocalModeValue, ActivityGraphItem):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class LocalModeCondition(LocalModeValue, Condition, IAnnotatable):

    relation = EAttribute(eType=RelationalOperator, unique=False, derived=False, changeable=True)

    def __init__(self, *, relation=None, **kwargs):

        super().__init__(**kwargs)

        if relation is not None:
            self.relation = relation


class DerivedTaggedobjects(EDerivedCollection):
    pass


class Tag(ReferableBaseObject, IDescription):
    """A tag for processes, runnables, events and labels"""
    tagType = EAttribute(eType=EString, unique=False, derived=False, changeable=True)
    taggedObjects = EReference(ordered=True, unique=True, containment=False,
                               derived=True, upper=-1, transient=True, derived_class=DerivedTaggedobjects)

    def __init__(self, *, tagType=None, taggedObjects=None, **kwargs):

        super().__init__(**kwargs)

        if tagType is not None:
            self.tagType = tagType

        if taggedObjects:
            self.taggedObjects.extend(taggedObjects)


@abstract
class Classifier(ReferableBaseObject, IDescription):
    """Classifiers for hardware properties"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class NumericMode(Mode):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class EnumMode(Mode):

    literals = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, literals=None, **kwargs):

        super().__init__(**kwargs)

        if literals:
            self.literals.extend(literals)

    def getLiteral(self, literal=None):

        raise NotImplementedError('operation getLiteral(...) not yet implemented')


@abstract
class ComponentInterface(ReferableBaseObject, ITaggable):

    datatype = EReference(ordered=True, unique=True, containment=False, derived=False)
    subInterfaces = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, datatype=None, subInterfaces=None, **kwargs):

        super().__init__(**kwargs)

        if datatype is not None:
            self.datatype = datatype

        if subInterfaces:
            self.subInterfaces.extend(subInterfaces)


class ComponentPort(ReferableBaseObject, ITaggable):

    kind = EAttribute(eType=InterfaceKind, unique=False, derived=False, changeable=True)
    containingComponent = EReference(ordered=True, unique=True, containment=False, derived=False)
    interface = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, containingComponent=None, kind=None, interface=None, **kwargs):

        super().__init__(**kwargs)

        if kind is not None:
            self.kind = kind

        if containingComponent is not None:
            self.containingComponent = containingComponent

        if interface is not None:
            self.interface = interface

    def getNamePrefixSegments(self):

        raise NotImplementedError('operation getNamePrefixSegments(...) not yet implemented')


class ComponentInstance(ReferableBaseObject, ITaggable):

    containingSystem = EReference(ordered=True, unique=True, containment=False, derived=False)
    type = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, containingSystem=None, type=None, **kwargs):

        super().__init__(**kwargs)

        if containingSystem is not None:
            self.containingSystem = containingSystem

        if type is not None:
            self.type = type

    def getNamePrefixSegments(self):

        raise NotImplementedError('operation getNamePrefixSegments(...) not yet implemented')


@abstract
class SeparationConstraint(AffinityConstraint):
    """An abstract superclass for all separation constraints"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class PairingConstraint(AffinityConstraint):
    """An abstract superclass for all pairing constraints"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class EventChain(AbstractEventChain, IReferable):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class SynchronizationConstraint(TimingConstraint):
    """Base class for synchronization constraints, which limit the distance between events
multipleOccurrencesAllowed: Defines whether multiple event occurrences are allowed for analysis
tolerance: Maximum allowed tolerance"""
    multipleOccurrencesAllowed = EAttribute(
        eType=EBoolean, unique=False, derived=False, changeable=True, default_value='false')
    tolerance = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, multipleOccurrencesAllowed=None, tolerance=None, **kwargs):

        super().__init__(**kwargs)

        if multipleOccurrencesAllowed is not None:
            self.multipleOccurrencesAllowed = multipleOccurrencesAllowed

        if tolerance is not None:
            self.tolerance = tolerance


class DelayConstraint(TimingConstraint):
    """This constraint describes how a source and a target event are placed relative to each other"""
    mappingType = EAttribute(eType=MappingType, unique=False, derived=False, changeable=True)
    source = EReference(ordered=True, unique=True, containment=False, derived=False)
    target = EReference(ordered=True, unique=True, containment=False, derived=False)
    upper = EReference(ordered=True, unique=True, containment=True, derived=False)
    lower = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, mappingType=None, source=None, target=None, upper=None, lower=None, **kwargs):

        super().__init__(**kwargs)

        if mappingType is not None:
            self.mappingType = mappingType

        if source is not None:
            self.source = source

        if target is not None:
            self.target = target

        if upper is not None:
            self.upper = upper

        if lower is not None:
            self.lower = lower


class EventChainLatencyConstraint(TimingConstraint):
    """A latency constraint describes the allowed range in latency between a stimulus and its response.
scope: Considered event chain that defines the stimulus and response relation
type: Defines the point of view (forward or backward)
minimum: Minimum allowed latency
maximum: Maximum allowed latency"""
    type = EAttribute(eType=LatencyType, unique=False, derived=False, changeable=True)
    scope = EReference(ordered=True, unique=True, containment=False, derived=False)
    minimum = EReference(ordered=True, unique=True, containment=True, derived=False)
    maximum = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, scope=None, type=None, minimum=None, maximum=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if scope is not None:
            self.scope = scope

        if minimum is not None:
            self.minimum = minimum

        if maximum is not None:
            self.maximum = maximum


class RepetitionConstraint(TimingConstraint):
    """A repetition constraint prescribes the distribution of a single event during runtime."""
    span = EAttribute(eType=EInt, unique=False, derived=False, changeable=True, default_value='0')
    event = EReference(ordered=True, unique=True, containment=False, derived=False)
    lower = EReference(ordered=True, unique=True, containment=True, derived=False)
    upper = EReference(ordered=True, unique=True, containment=True, derived=False)
    jitter = EReference(ordered=True, unique=True, containment=True, derived=False)
    period = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, event=None, span=None, lower=None, upper=None, jitter=None, period=None, **kwargs):

        super().__init__(**kwargs)

        if span is not None:
            self.span = span

        if event is not None:
            self.event = event

        if lower is not None:
            self.lower = lower

        if upper is not None:
            self.upper = upper

        if jitter is not None:
            self.jitter = jitter

        if period is not None:
            self.period = period


class DerivedInnerports(EDerivedCollection):
    pass


class HwStructure(ReferableBaseObject, ITaggable):

    structureType = EAttribute(eType=StructureType, unique=False, derived=False, changeable=True)
    ports = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    structures = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    modules = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    connections = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    innerPorts = EReference(ordered=True, unique=True, containment=False,
                            derived=True, upper=-1, transient=True, derived_class=DerivedInnerports)

    def __init__(self, *, structureType=None, ports=None, structures=None, modules=None, connections=None, innerPorts=None, **kwargs):

        super().__init__(**kwargs)

        if structureType is not None:
            self.structureType = structureType

        if ports:
            self.ports.extend(ports)

        if structures:
            self.structures.extend(structures)

        if modules:
            self.modules.extend(modules)

        if connections:
            self.connections.extend(connections)

        if innerPorts:
            self.innerPorts.extend(innerPorts)


@abstract
class HwModule(ReferableBaseObject, ITaggable):

    ports = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    powerDomain = EReference(ordered=True, unique=True, containment=False, derived=False)
    frequencyDomain = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, ports=None, powerDomain=None, frequencyDomain=None, **kwargs):

        super().__init__(**kwargs)

        if ports:
            self.ports.extend(ports)

        if powerDomain is not None:
            self.powerDomain = powerDomain

        if frequencyDomain is not None:
            self.frequencyDomain = frequencyDomain


@abstract
class HwDomain(ReferableBaseObject, ITaggable):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class HwFeatureCategory(ReferableBaseObject, IDescription):

    featureType = EAttribute(eType=HwFeatureType, unique=False, derived=False, changeable=True)
    features = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, featureType=None, features=None, **kwargs):

        super().__init__(**kwargs)

        if featureType is not None:
            self.featureType = featureType

        if features:
            self.features.extend(features)


class DerivedConnections(EDerivedCollection):
    pass


class HwPort(ReferableBaseObject, ITaggable):

    bitWidth = EAttribute(eType=EInt, unique=False, derived=False,
                          changeable=True, default_value='0')
    priority = EAttribute(eType=EInt, unique=False, derived=False,
                          changeable=True, default_value='0')
    portType = EAttribute(eType=PortType, unique=False, derived=False, changeable=True)
    portInterface = EAttribute(eType=PortInterface, unique=False, derived=False, changeable=True)
    _delegated = EAttribute(eType=EBoolean, unique=False, derived=True,
                            changeable=False, name='delegated', transient=True)
    connections = EReference(ordered=True, unique=True, containment=False,
                             derived=True, upper=-1, transient=True, derived_class=DerivedConnections)

    @property
    def delegated(self):
        raise NotImplementedError('Missing implementation for delegated')

    def __init__(self, *, bitWidth=None, priority=None, portType=None, portInterface=None, delegated=None, connections=None, **kwargs):

        super().__init__(**kwargs)

        if bitWidth is not None:
            self.bitWidth = bitWidth

        if priority is not None:
            self.priority = priority

        if portType is not None:
            self.portType = portType

        if portInterface is not None:
            self.portInterface = portInterface

        if delegated is not None:
            self.delegated = delegated

        if connections:
            self.connections.extend(connections)

    def getNamePrefixSegments(self):

        raise NotImplementedError('operation getNamePrefixSegments(...) not yet implemented')


@abstract
class HwDefinition(ReferableBaseObject, ITaggable):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DerivedSchedulerallocations(EDerivedCollection):
    pass


class DerivedRunnableallocations(EDerivedCollection):
    pass


@abstract
class Scheduler(ReferableBaseObject, ISchedulingParameterContainer):
    """Scheduler
<ul>
<li>definition: determines algorithm for scheduling and its required parameters</li>
<li>schedulingParameters: current values for global scheduling parameters</li>
<li>computation items: steps to perform the scheduling algorithm</li>
</ul>"""
    definition = EReference(ordered=True, unique=True, containment=False, derived=False)
    computationItems = EReference(ordered=True, unique=True,
                                  containment=True, derived=False, upper=-1)
    schedulerAllocations = EReference(ordered=True, unique=True, containment=False,
                                      derived=True, upper=-1, transient=True, derived_class=DerivedSchedulerallocations)
    runnableAllocations = EReference(ordered=True, unique=True, containment=False,
                                     derived=True, upper=-1, transient=True, derived_class=DerivedRunnableallocations)

    def __init__(self, *, definition=None, computationItems=None, schedulerAllocations=None, runnableAllocations=None, **kwargs):

        super().__init__(**kwargs)

        if definition is not None:
            self.definition = definition

        if computationItems:
            self.computationItems.extend(computationItems)

        if schedulerAllocations:
            self.schedulerAllocations.extend(schedulerAllocations)

        if runnableAllocations:
            self.runnableAllocations.extend(runnableAllocations)


@abstract
class OsDefinition(ReferableBaseObject, ITaggable):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DerivedAffectedprocesses(EDerivedCollection):
    pass


@abstract
class Stimulus(ReferableBaseObject, ITaggable):
    """Every process/task can have one or more stimuli.
A stimulus activates the process"""
    setModeValueList = EReference(ordered=True, unique=True, containment=True, derived=False)
    executionCondition = EReference(ordered=True, unique=True, containment=True, derived=False)
    affectedProcesses = EReference(ordered=True, unique=True, containment=False,
                                   derived=True, upper=-1, transient=True, derived_class=DerivedAffectedprocesses)

    def __init__(self, *, setModeValueList=None, executionCondition=None, affectedProcesses=None, **kwargs):

        super().__init__(**kwargs)

        if setModeValueList is not None:
            self.setModeValueList = setModeValueList

        if executionCondition is not None:
            self.executionCondition = executionCondition

        if affectedProcesses:
            self.affectedProcesses.extend(affectedProcesses)


class ClockFunction(Clock):

    curveType = EAttribute(eType=CurveType, unique=False, derived=False, changeable=True)
    period = EReference(ordered=True, unique=True, containment=True, derived=False)
    peakToPeak = EReference(ordered=True, unique=True, containment=True, derived=False)
    xOffset = EReference(ordered=True, unique=True, containment=True, derived=False)
    yOffset = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, curveType=None, period=None, peakToPeak=None, xOffset=None, yOffset=None, **kwargs):

        super().__init__(**kwargs)

        if curveType is not None:
            self.curveType = curveType

        if period is not None:
            self.period = period

        if peakToPeak is not None:
            self.peakToPeak = peakToPeak

        if xOffset is not None:
            self.xOffset = xOffset

        if yOffset is not None:
            self.yOffset = yOffset


class ClockStepList(Clock):

    entries = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    period = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, entries=None, period=None, **kwargs):

        super().__init__(**kwargs)

        if entries:
            self.entries.extend(entries)

        if period is not None:
            self.period = period


class DerivedMappings(EDerivedCollection):
    pass


@abstract
class AbstractMemoryElement(ReferableBaseObject, ITaggable):

    size = EReference(ordered=True, unique=True, containment=True, derived=False)
    mappings = EReference(ordered=True, unique=True, containment=False,
                          derived=True, upper=-1, transient=True, derived_class=DerivedMappings)

    def __init__(self, *, size=None, mappings=None, **kwargs):

        super().__init__(**kwargs)

        if size is not None:
            self.size = size

        if mappings:
            self.mappings.extend(mappings)


class DerivedReferringcomponents(EDerivedCollection):
    pass


class OsEvent(ReferableBaseObject, ITaggable):
    """A event that can be set, cleared and waited for by a process"""
    communicationOverheadInBit = EAttribute(
        eType=EInt, unique=False, derived=False, changeable=True, default_value='0')
    referringComponents = EReference(ordered=True, unique=True, containment=False,
                                     derived=True, upper=-1, transient=True, derived_class=DerivedReferringcomponents)

    def __init__(self, *, communicationOverheadInBit=None, referringComponents=None, **kwargs):

        super().__init__(**kwargs)

        if communicationOverheadInBit is not None:
            self.communicationOverheadInBit = communicationOverheadInBit

        if referringComponents:
            self.referringComponents.extend(referringComponents)


class RunnableParameter(ReferableBaseObject, IDependsOn):

    direction = EAttribute(eType=DirectionType, unique=False, derived=False, changeable=True)
    containingRunnable = EReference(ordered=True, unique=True, containment=False, derived=False)
    dataType = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, containingRunnable=None, direction=None, dataType=None, **kwargs):

        super().__init__(**kwargs)

        if direction is not None:
            self.direction = direction

        if containingRunnable is not None:
            self.containingRunnable = containingRunnable

        if dataType is not None:
            self.dataType = dataType

    def getNamePrefixSegments(self):

        raise NotImplementedError('operation getNamePrefixSegments(...) not yet implemented')

    def toString(self):

        raise NotImplementedError('operation toString(...) not yet implemented')


class Group(ActivityGraphItem, INamed, IActivityGraphItemContainer):
    """Describes a group of deviation runnable items"""
    ordered = EAttribute(eType=EBoolean, unique=False, derived=False,
                         changeable=True, default_value='true')
    interruptible = EAttribute(eType=EBoolean, unique=False, derived=False,
                               changeable=True, default_value='true')

    def __init__(self, *, ordered=None, interruptible=None, **kwargs):

        super().__init__(**kwargs)

        if ordered is not None:
            self.ordered = ordered

        if interruptible is not None:
            self.interruptible = interruptible


class Struct(CompoundType, ITaggable):
    """Representing a struct definition, containing different entries"""
    entries = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, entries=None, **kwargs):

        super().__init__(**kwargs)

        if entries:
            self.entries.extend(entries)


@abstract
class TypeDefinition(ReferableBaseObject, INamespaceMember):

    size = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, size=None, **kwargs):

        super().__init__(**kwargs)

        if size is not None:
            self.size = size


@abstract
class Activation(ReferableBaseObject, ITaggable):
    """General abstraction for activation source.
Used for first definition of an activation rate, which is later refined by stimulus."""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class CoreClassifier(Classifier):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class MemoryClassifier(Classifier):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class SubInterface(ComponentInterface):

    containingInterface = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, containingInterface=None, **kwargs):

        super().__init__(**kwargs)

        if containingInterface is not None:
            self.containingInterface = containingInterface

    def getNamePrefixSegments(self):

        raise NotImplementedError('operation getNamePrefixSegments(...) not yet implemented')


class System(ReferableBaseObject, ITaggable, ISystem):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class EventSynchronizationConstraint(SynchronizationConstraint):
    """The synchronization constraint considers a group of events and limits the distance of the events within this group."""
    events = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, events=None, **kwargs):

        super().__init__(**kwargs)

        if events:
            self.events.extend(events)


class EventChainSynchronizationConstraint(SynchronizationConstraint):
    """A synchronization constraint describes the allowed tolerance in synchronization between two event chains
scope: Considered event chains that have to by in sync
type: Defines which parts of the event chains have to be in sync"""
    type = EAttribute(eType=SynchronizationType, unique=False, derived=False, changeable=True)
    scope = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, scope=None, type=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if scope:
            self.scope.extend(scope)


@abstract
class Event(ReferableBaseObject, ITaggable, IDescription):
    """An abstract event"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class FrequencyDomain(HwDomain):

    clockGating = EAttribute(eType=EBoolean, unique=False, derived=False,
                             changeable=True, default_value='false')
    defaultValue = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, defaultValue=None, clockGating=None, **kwargs):

        super().__init__(**kwargs)

        if clockGating is not None:
            self.clockGating = clockGating

        if defaultValue is not None:
            self.defaultValue = defaultValue


class PowerDomain(HwDomain):

    powerGating = EAttribute(eType=EBoolean, unique=False, derived=False,
                             changeable=True, default_value='false')
    defaultValue = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, defaultValue=None, powerGating=None, **kwargs):

        super().__init__(**kwargs)

        if powerGating is not None:
            self.powerGating = powerGating

        if defaultValue is not None:
            self.defaultValue = defaultValue


class HwConnection(ReferableBaseObject, HwPathElement, ITaggable):

    _internal = EAttribute(eType=EBoolean, unique=False, derived=True,
                           changeable=False, name='internal', transient=True)
    readLatency = EReference(ordered=True, unique=True, containment=True, derived=False)
    writeLatency = EReference(ordered=True, unique=True, containment=True, derived=False)
    dataRate = EReference(ordered=True, unique=True, containment=True, derived=False)
    port1 = EReference(ordered=True, unique=True, containment=False, derived=False)
    port2 = EReference(ordered=True, unique=True, containment=False, derived=False)

    @property
    def internal(self):
        raise NotImplementedError('Missing implementation for internal')

    def __init__(self, *, readLatency=None, writeLatency=None, dataRate=None, port1=None, port2=None, internal=None, **kwargs):

        super().__init__(**kwargs)

        if internal is not None:
            self.internal = internal

        if readLatency is not None:
            self.readLatency = readLatency

        if writeLatency is not None:
            self.writeLatency = writeLatency

        if dataRate is not None:
            self.dataRate = dataRate

        if port1 is not None:
            self.port1 = port1

        if port2 is not None:
            self.port2 = port2

    def getNamePrefixSegments(self):

        raise NotImplementedError('operation getNamePrefixSegments(...) not yet implemented')

    def getPorts(self):

        raise NotImplementedError('operation getPorts(...) not yet implemented')


class ProcessingUnitDefinition(HwDefinition):

    puType = EAttribute(eType=PuType, unique=False, derived=False, changeable=True)
    features = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    classifiers = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, puType=None, features=None, classifiers=None, **kwargs):

        super().__init__(**kwargs)

        if puType is not None:
            self.puType = puType

        if features:
            self.features.extend(features)

        if classifiers:
            self.classifiers.extend(classifiers)


class ConnectionHandlerDefinition(HwDefinition):

    policy = EAttribute(eType=SchedPolicy, unique=False, derived=False, changeable=True)
    maxBurstSize = EAttribute(eType=PositiveInt, unique=False,
                              derived=False, changeable=True, default_value='1')
    maxConcurrentTransfers = EAttribute(
        eType=PositiveInt, unique=False, derived=False, changeable=True, default_value='1')
    readLatency = EReference(ordered=True, unique=True, containment=True, derived=False)
    writeLatency = EReference(ordered=True, unique=True, containment=True, derived=False)
    dataRate = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, policy=None, readLatency=None, writeLatency=None, dataRate=None, maxBurstSize=None, maxConcurrentTransfers=None, **kwargs):

        super().__init__(**kwargs)

        if policy is not None:
            self.policy = policy

        if maxBurstSize is not None:
            self.maxBurstSize = maxBurstSize

        if maxConcurrentTransfers is not None:
            self.maxConcurrentTransfers = maxConcurrentTransfers

        if readLatency is not None:
            self.readLatency = readLatency

        if writeLatency is not None:
            self.writeLatency = writeLatency

        if dataRate is not None:
            self.dataRate = dataRate


class MemoryDefinition(HwDefinition):

    memoryType = EAttribute(eType=MemoryType, unique=False, derived=False, changeable=True)
    size = EReference(ordered=True, unique=True, containment=True, derived=False)
    accessLatency = EReference(ordered=True, unique=True, containment=True, derived=False)
    dataRate = EReference(ordered=True, unique=True, containment=True, derived=False)
    classifiers = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, size=None, accessLatency=None, dataRate=None, memoryType=None, classifiers=None, **kwargs):

        super().__init__(**kwargs)

        if memoryType is not None:
            self.memoryType = memoryType

        if size is not None:
            self.size = size

        if accessLatency is not None:
            self.accessLatency = accessLatency

        if dataRate is not None:
            self.dataRate = dataRate

        if classifiers:
            self.classifiers.extend(classifiers)


class CacheDefinition(HwDefinition):

    cacheType = EAttribute(eType=CacheType, unique=False, derived=False, changeable=True)
    writeStrategy = EAttribute(eType=WriteStrategy, unique=False, derived=False, changeable=True)
    nWays = EAttribute(eType=EInt, unique=False, derived=False, changeable=True, default_value='0')
    coherency = EAttribute(eType=EBoolean, unique=False, derived=False,
                           changeable=True, default_value='false')
    exclusive = EAttribute(eType=EBoolean, unique=False, derived=False,
                           changeable=True, default_value='false')
    hitRate = EAttribute(eType=EDouble, unique=False, derived=False,
                         changeable=True, default_value='0.0')
    size = EReference(ordered=True, unique=True, containment=True, derived=False)
    lineSize = EReference(ordered=True, unique=True, containment=True, derived=False)
    accessLatency = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, size=None, lineSize=None, accessLatency=None, cacheType=None, writeStrategy=None, nWays=None, coherency=None, exclusive=None, hitRate=None, **kwargs):

        super().__init__(**kwargs)

        if cacheType is not None:
            self.cacheType = cacheType

        if writeStrategy is not None:
            self.writeStrategy = writeStrategy

        if nWays is not None:
            self.nWays = nWays

        if coherency is not None:
            self.coherency = coherency

        if exclusive is not None:
            self.exclusive = exclusive

        if hitRate is not None:
            self.hitRate = hitRate

        if size is not None:
            self.size = size

        if lineSize is not None:
            self.lineSize = lineSize

        if accessLatency is not None:
            self.accessLatency = accessLatency


class DerivedChildassociations(EDerivedCollection):
    pass


class DerivedTaskallocations(EDerivedCollection):
    pass


class DerivedChildschedulers(EDerivedCollection):
    pass


class TaskScheduler(Scheduler):

    parentAssociation = EReference(ordered=True, unique=True, containment=True, derived=False)
    childAssociations = EReference(ordered=True, unique=True, containment=False,
                                   derived=True, upper=-1, transient=True, derived_class=DerivedChildassociations)
    taskAllocations = EReference(ordered=True, unique=True, containment=False,
                                 derived=True, upper=-1, transient=True, derived_class=DerivedTaskallocations)
    _parentScheduler = EReference(ordered=True, unique=True, containment=False,
                                  derived=True, name='parentScheduler', transient=True)
    childSchedulers = EReference(ordered=True, unique=True, containment=False,
                                 derived=True, upper=-1, transient=True, derived_class=DerivedChildschedulers)

    @property
    def parentScheduler(self):
        raise NotImplementedError('Missing implementation for parentScheduler')

    def __init__(self, *, parentAssociation=None, childAssociations=None, taskAllocations=None, parentScheduler=None, childSchedulers=None, **kwargs):

        super().__init__(**kwargs)

        if parentAssociation is not None:
            self.parentAssociation = parentAssociation

        if childAssociations:
            self.childAssociations.extend(childAssociations)

        if taskAllocations:
            self.taskAllocations.extend(taskAllocations)

        if parentScheduler is not None:
            self.parentScheduler = parentScheduler

        if childSchedulers:
            self.childSchedulers.extend(childSchedulers)


class DerivedIsrallocations(EDerivedCollection):
    pass


class InterruptController(Scheduler):

    isrAllocations = EReference(ordered=True, unique=True, containment=False,
                                derived=True, upper=-1, transient=True, derived_class=DerivedIsrallocations)

    def __init__(self, *, isrAllocations=None, **kwargs):

        super().__init__(**kwargs)

        if isrAllocations:
            self.isrAllocations.extend(isrAllocations)


class DerivedSchedulerdefinitions(EDerivedCollection):
    pass


class SchedulingParameterDefinition(OsDefinition):

    type = EAttribute(eType=ParameterType, unique=False, derived=False, changeable=True)
    many = EAttribute(eType=EBoolean, unique=False, derived=False,
                      changeable=True, default_value='false')
    mandatory = EAttribute(eType=EBoolean, unique=False, derived=False,
                           changeable=True, default_value='true')
    defaultValue = EReference(ordered=True, unique=True, containment=True, derived=False)
    schedulerDefinitions = EReference(ordered=True, unique=True, containment=False,
                                      derived=True, upper=-1, transient=True, derived_class=DerivedSchedulerdefinitions)

    def __init__(self, *, type=None, many=None, mandatory=None, defaultValue=None, schedulerDefinitions=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if many is not None:
            self.many = many

        if mandatory is not None:
            self.mandatory = mandatory

        if defaultValue is not None:
            self.defaultValue = defaultValue

        if schedulerDefinitions:
            self.schedulerDefinitions.extend(schedulerDefinitions)


class OsOverhead(OsDefinition):

    apiOverhead = EReference(ordered=True, unique=True, containment=True, derived=False)
    isrCategory1Overhead = EReference(ordered=True, unique=True, containment=True, derived=False)
    isrCategory2Overhead = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, apiOverhead=None, isrCategory1Overhead=None, isrCategory2Overhead=None, **kwargs):

        super().__init__(**kwargs)

        if apiOverhead is not None:
            self.apiOverhead = apiOverhead

        if isrCategory1Overhead is not None:
            self.isrCategory1Overhead = isrCategory1Overhead

        if isrCategory2Overhead is not None:
            self.isrCategory2Overhead = isrCategory2Overhead


class RelativePeriodicStimulus(Stimulus):
    """Stimulus that is triggered relative to the previous occurrence.
offset: Time of first occurrence
step: Time (Deviation) between successive occurrences"""
    offset = EReference(ordered=True, unique=True, containment=True, derived=False)
    nextOccurrence = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, offset=None, nextOccurrence=None, **kwargs):

        super().__init__(**kwargs)

        if offset is not None:
            self.offset = offset

        if nextOccurrence is not None:
            self.nextOccurrence = nextOccurrence


class VariableRateStimulus(Stimulus):
    """Periodic stimulus based on other events, like rotation speed
clock: Time base which defines deviation of time, multiple stimuli can have the same time base"""
    maxIncreasePerStep = EAttribute(eType=EDoubleObject, unique=False,
                                    derived=False, changeable=True)
    maxDecreasePerStep = EAttribute(eType=EDoubleObject, unique=False,
                                    derived=False, changeable=True)
    step = EReference(ordered=True, unique=True, containment=True, derived=False)
    occurrencesPerStep = EReference(ordered=True, unique=True, containment=True, derived=False)
    scenario = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, step=None, occurrencesPerStep=None, maxIncreasePerStep=None, maxDecreasePerStep=None, scenario=None, **kwargs):

        super().__init__(**kwargs)

        if maxIncreasePerStep is not None:
            self.maxIncreasePerStep = maxIncreasePerStep

        if maxDecreasePerStep is not None:
            self.maxDecreasePerStep = maxDecreasePerStep

        if step is not None:
            self.step = step

        if occurrencesPerStep is not None:
            self.occurrencesPerStep = occurrencesPerStep

        if scenario is not None:
            self.scenario = scenario


class SingleStimulus(Stimulus):
    """Single occurrence at a defined time."""
    occurrence = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, occurrence=None, **kwargs):

        super().__init__(**kwargs)

        if occurrence is not None:
            self.occurrence = occurrence


class DerivedExplicittriggers(EDerivedCollection):
    pass


class InterProcessStimulus(Stimulus):
    """Stimulus based on a explicit inter process trigger."""
    counter = EReference(ordered=True, unique=True, containment=True, derived=False)
    explicitTriggers = EReference(ordered=True, unique=True, containment=False,
                                  derived=True, upper=-1, transient=True, derived_class=DerivedExplicittriggers)

    def __init__(self, *, counter=None, explicitTriggers=None, **kwargs):

        super().__init__(**kwargs)

        if counter is not None:
            self.counter = counter

        if explicitTriggers:
            self.explicitTriggers.extend(explicitTriggers)


class EventStimulus(Stimulus):
    """Stimulus which is activated by an event."""
    triggeringEvents = EReference(ordered=True, unique=True,
                                  containment=False, derived=False, upper=-1)
    counter = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, triggeringEvents=None, counter=None, **kwargs):

        super().__init__(**kwargs)

        if triggeringEvents:
            self.triggeringEvents.extend(triggeringEvents)

        if counter is not None:
            self.counter = counter


class ArrivalCurveStimulus(Stimulus):
    """Arrival Curve Stimulus"""
    entries = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, entries=None, **kwargs):

        super().__init__(**kwargs)

        if entries:
            self.entries.extend(entries)


class DerivedReferringcomponents(EDerivedCollection):
    pass


@abstract
class AbstractProcess(AbstractMemoryElement):

    referringComponents = EReference(ordered=True, unique=True, containment=False,
                                     derived=True, upper=-1, transient=True, derived_class=DerivedReferringcomponents)

    def __init__(self, *, referringComponents=None, **kwargs):

        super().__init__(**kwargs)

        if referringComponents:
            self.referringComponents.extend(referringComponents)


class LabelAccess(ComputationItem, ITaggable, IDependsOn):
    """Representation of a label access of a run entity."""
    access = EAttribute(eType=LabelAccessEnum, unique=False, derived=False, changeable=True)
    dataStability = EAttribute(eType=LabelAccessDataStability,
                               unique=False, derived=False, changeable=True)
    implementation = EAttribute(eType=LabelAccessImplementation,
                                unique=False, derived=False, changeable=True)
    data = EReference(ordered=True, unique=True, containment=False, derived=False)
    statistic = EReference(ordered=True, unique=True, containment=True, derived=False)
    transmissionPolicy = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, data=None, access=None, statistic=None, transmissionPolicy=None, dataStability=None, implementation=None, **kwargs):

        super().__init__(**kwargs)

        if access is not None:
            self.access = access

        if dataStability is not None:
            self.dataStability = dataStability

        if implementation is not None:
            self.implementation = implementation

        if data is not None:
            self.data = data

        if statistic is not None:
            self.statistic = statistic

        if transmissionPolicy is not None:
            self.transmissionPolicy = transmissionPolicy


class DataTypeDefinition(TypeDefinition):

    dataType = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, dataType=None, **kwargs):

        super().__init__(**kwargs)

        if dataType is not None:
            self.dataType = dataType


class BaseTypeDefinition(TypeDefinition):
    """Basic data type definition, including naming (alias) in target environments"""
    aliases = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, aliases=None, **kwargs):

        super().__init__(**kwargs)

        if aliases:
            self.aliases.extend(aliases)


class PeriodicActivation(Activation):
    """Min and Max execution frequency within a task or timeslice"""
    min = EReference(ordered=True, unique=True, containment=True, derived=False)
    max = EReference(ordered=True, unique=True, containment=True, derived=False)
    recurrence = EReference(ordered=True, unique=True, containment=True, derived=False)
    offset = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, min=None, max=None, recurrence=None, offset=None, **kwargs):

        super().__init__(**kwargs)

        if min is not None:
            self.min = min

        if max is not None:
            self.max = max

        if recurrence is not None:
            self.recurrence = recurrence

        if offset is not None:
            self.offset = offset


class SingleActivation(Activation):
    """A single activation between time min and max"""
    min = EReference(ordered=True, unique=True, containment=True, derived=False)
    max = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, min=None, max=None, **kwargs):

        super().__init__(**kwargs)

        if min is not None:
            self.min = min

        if max is not None:
            self.max = max


class EventActivation(Activation):
    """Activation which is triggered by an event."""
    triggeringEvents = EReference(ordered=True, unique=True,
                                  containment=False, derived=False, upper=-1)
    counter = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, triggeringEvents=None, counter=None, **kwargs):

        super().__init__(**kwargs)

        if triggeringEvents:
            self.triggeringEvents.extend(triggeringEvents)

        if counter is not None:
            self.counter = counter


class Component(ReferableBaseObject, ITaggable, INamespaceMember, IComponentStructureMember):

    ports = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    processes = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    runnables = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    labels = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    semaphores = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    osEvents = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, ports=None, processes=None, runnables=None, labels=None, semaphores=None, osEvents=None, **kwargs):

        super().__init__(**kwargs)

        if ports:
            self.ports.extend(ports)

        if processes:
            self.processes.extend(processes)

        if runnables:
            self.runnables.extend(runnables)

        if labels:
            self.labels.extend(labels)

        if semaphores:
            self.semaphores.extend(semaphores)

        if osEvents:
            self.osEvents.extend(osEvents)


class EventSet(Event):
    """A set of entity-events"""
    events = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, events=None, **kwargs):

        super().__init__(**kwargs)

        if events:
            self.events.extend(events)


@abstract
class EntityEvent(Event):
    """An abstract event that describes the notification of a changed state of an entity"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DerivedMappings(EDerivedCollection):
    pass


class Memory(HwModule, HwDestination):

    definition = EReference(ordered=True, unique=True, containment=False, derived=False)
    mappings = EReference(ordered=True, unique=True, containment=False,
                          derived=True, upper=-1, transient=True, derived_class=DerivedMappings)

    def __init__(self, *, definition=None, mappings=None, **kwargs):

        super().__init__(**kwargs)

        if definition is not None:
            self.definition = definition

        if mappings:
            self.mappings.extend(mappings)


class Cache(HwModule, HwPathElement):

    definition = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, definition=None, **kwargs):

        super().__init__(**kwargs)

        if definition is not None:
            self.definition = definition


class ConnectionHandler(HwModule, HwPathElement):

    definition = EReference(ordered=True, unique=True, containment=False, derived=False)
    internalConnections = EReference(ordered=True, unique=True,
                                     containment=True, derived=False, upper=-1)

    def __init__(self, *, definition=None, internalConnections=None, **kwargs):

        super().__init__(**kwargs)

        if definition is not None:
            self.definition = definition

        if internalConnections:
            self.internalConnections.extend(internalConnections)


class SchedulerDefinition(OsDefinition, IDescription):

    requiresParentScheduler = EAttribute(
        eType=EBoolean, unique=False, derived=False, changeable=True, default_value='false')
    passesParametersUpwards = EAttribute(
        eType=EBoolean, unique=False, derived=False, changeable=True, default_value='false')
    hasExactlyOneChild = EAttribute(eType=EBoolean, unique=False,
                                    derived=False, changeable=True, default_value='false')
    algorithmParameters = EReference(ordered=True, unique=True,
                                     containment=False, derived=False, upper=-1)
    processParameters = EReference(ordered=True, unique=True,
                                   containment=False, derived=False, upper=-1)

    def __init__(self, *, algorithmParameters=None, processParameters=None, requiresParentScheduler=None, passesParametersUpwards=None, hasExactlyOneChild=None, **kwargs):

        super().__init__(**kwargs)

        if requiresParentScheduler is not None:
            self.requiresParentScheduler = requiresParentScheduler

        if passesParametersUpwards is not None:
            self.passesParametersUpwards = passesParametersUpwards

        if hasExactlyOneChild is not None:
            self.hasExactlyOneChild = hasExactlyOneChild

        if algorithmParameters:
            self.algorithmParameters.extend(algorithmParameters)

        if processParameters:
            self.processParameters.extend(processParameters)


class ModeLabelCondition(BaseObject, ModeCondition):

    label1 = EReference(ordered=True, unique=True, containment=False, derived=False)
    label2 = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, label1=None, label2=None, **kwargs):

        super().__init__(**kwargs)

        if label1 is not None:
            self.label1 = label1

        if label2 is not None:
            self.label2 = label2

    def isSatisfiedBy(self, context=None):

        raise NotImplementedError('operation isSatisfiedBy(...) not yet implemented')

    def validateInvariants(self, diagnostics=None, context=None):

        raise NotImplementedError('operation validateInvariants(...) not yet implemented')


class PeriodicStimulus(Stimulus, FixedPeriodic):
    """Stimulus that is triggered periodically.
jitter: Deviation from true periodicity to real occurrence
minDistance: Minimal time between occurrences"""
    jitter = EReference(ordered=True, unique=True, containment=True, derived=False)
    minDistance = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, jitter=None, minDistance=None, **kwargs):

        super().__init__(**kwargs)

        if jitter is not None:
            self.jitter = jitter

        if minDistance is not None:
            self.minDistance = minDistance


class PeriodicSyntheticStimulus(Stimulus, FixedPeriodic):
    """Stimulus (repeated periodically) with a defined list of occurrences.
occurrenceTimes: List of all occurrences"""
    occurrenceTimes = EReference(ordered=True, unique=True,
                                 containment=True, derived=False, upper=-1)

    def __init__(self, *, occurrenceTimes=None, **kwargs):

        super().__init__(**kwargs)

        if occurrenceTimes:
            self.occurrenceTimes.extend(occurrenceTimes)


class CustomStimulus(Stimulus, IDescription):
    """Stimulus to describe own custom types, including properties."""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class PeriodicBurstStimulus(Stimulus, FixedPeriodic):
    """Stimulus  (repeated periodically) for burst occurrences
burstLength: Time frame for the burst (occurrences after the length are clipped)"""
    occurrenceCount = EAttribute(eType=PositiveInt, unique=False,
                                 derived=False, changeable=True, default_value='1')
    burstLength = EReference(ordered=True, unique=True, containment=True, derived=False)
    occurrenceMinDistance = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, burstLength=None, occurrenceMinDistance=None, occurrenceCount=None, **kwargs):

        super().__init__(**kwargs)

        if occurrenceCount is not None:
            self.occurrenceCount = occurrenceCount

        if burstLength is not None:
            self.burstLength = burstLength

        if occurrenceMinDistance is not None:
            self.occurrenceMinDistance = occurrenceMinDistance


class CustomEntity(AbstractMemoryElement, IDescription):
    """Possibility to define general custom elements"""
    typeName = EAttribute(eType=EString, unique=False, derived=False, changeable=True)

    def __init__(self, *, typeName=None, **kwargs):

        super().__init__(**kwargs)

        if typeName is not None:
            self.typeName = typeName


class ProcessPrototype(AbstractProcess):
    """Prototype class for Process.
It does contain meta information of potential processes, which does not represent the final state.
The final state can be several Tasks, which can be computed using provided information of this prototype."""
    preemption = EAttribute(eType=Preemption, unique=False, derived=False, changeable=True)
    firstRunnable = EReference(ordered=True, unique=True, containment=False, derived=False)
    lastRunnable = EReference(ordered=True, unique=True, containment=False, derived=False)
    accessPrecedenceSpec = EReference(ordered=True, unique=True,
                                      containment=True, derived=False, upper=-1)
    orderPrecedenceSpec = EReference(ordered=True, unique=True,
                                     containment=True, derived=False, upper=-1)
    chainedPrototypes = EReference(ordered=True, unique=True,
                                   containment=True, derived=False, upper=-1)
    activation = EReference(ordered=True, unique=True, containment=False, derived=False)
    runnableCalls = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, preemption=None, firstRunnable=None, lastRunnable=None, accessPrecedenceSpec=None, orderPrecedenceSpec=None, chainedPrototypes=None, activation=None, runnableCalls=None, **kwargs):

        super().__init__(**kwargs)

        if preemption is not None:
            self.preemption = preemption

        if firstRunnable is not None:
            self.firstRunnable = firstRunnable

        if lastRunnable is not None:
            self.lastRunnable = lastRunnable

        if accessPrecedenceSpec:
            self.accessPrecedenceSpec.extend(accessPrecedenceSpec)

        if orderPrecedenceSpec:
            self.orderPrecedenceSpec.extend(orderPrecedenceSpec)

        if chainedPrototypes:
            self.chainedPrototypes.extend(chainedPrototypes)

        if activation is not None:
            self.activation = activation

        if runnableCalls:
            self.runnableCalls.extend(runnableCalls)


class ModeLabel(AbstractMemoryElement, IDisplayName):

    initialValue = EAttribute(eType=EString, unique=False, derived=False, changeable=True)
    mode = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, mode=None, initialValue=None, **kwargs):

        super().__init__(**kwargs)

        if initialValue is not None:
            self.initialValue = initialValue

        if mode is not None:
            self.mode = mode

    def validateInvariants(self, diagnostics=None, context=None):

        raise NotImplementedError('operation validateInvariants(...) not yet implemented')

    def isEnum(self):

        raise NotImplementedError('operation isEnum(...) not yet implemented')

    def isNumeric(self):

        raise NotImplementedError('operation isNumeric(...) not yet implemented')


class VariableRateActivation(Activation, IDescription):
    """Periodic activation based on other events, like rotation speed"""
    step = EReference(ordered=True, unique=True, containment=True, derived=False)
    occurrencesPerStep = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, step=None, occurrencesPerStep=None, **kwargs):

        super().__init__(**kwargs)

        if step is not None:
            self.step = step

        if occurrencesPerStep is not None:
            self.occurrencesPerStep = occurrencesPerStep


class SporadicActivation(Activation, IDescription):

    occurrence = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, occurrence=None, **kwargs):

        super().__init__(**kwargs)

        if occurrence is not None:
            self.occurrence = occurrence


class CustomActivation(Activation, IDescription):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class MainInterface(ComponentInterface, INamespaceMember, IComponentStructureMember):

    version = EAttribute(eType=EString, unique=False, derived=False,
                         changeable=True, default_value='1.0')

    def __init__(self, *, version=None, **kwargs):

        super().__init__(**kwargs)

        if version is not None:
            self.version = version


class RunnableSeparationConstraint(SeparationConstraint, RunnableConstraint, BaseObject):
    """A runnable-separation-constraint
groups describes the runnable-groups that should be separated from each other on the target
if there is only one group then this means that the runnables of this group are not allowed to be executed on the target"""
    groups = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, groups=None, **kwargs):

        super().__init__(**kwargs)

        if groups:
            self.groups.extend(groups)


class ProcessSeparationConstraint(SeparationConstraint, ProcessConstraint, BaseObject):
    """A process-separation-constraint
groups describes the process-groups that should be separated from each other on the target
if there is only one group then this means that the processes of this group are not allowed to be executed on the target"""
    groups = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, groups=None, **kwargs):

        super().__init__(**kwargs)

        if groups:
            self.groups.extend(groups)


class DataSeparationConstraint(SeparationConstraint, DataConstraint, BaseObject):
    """A data-separation-constraint
groups describes the label-groups that should be separated from each other on the target
if there is only one group then this means that the label of this group is not allowed to be executed on the target"""
    groups = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, groups=None, **kwargs):

        super().__init__(**kwargs)

        if groups:
            self.groups.extend(groups)


class RunnablePairingConstraint(PairingConstraint, RunnableConstraint, BaseObject):
    """A runnable-pairing-constraint
runnables describes the group of runnables that should be paired on the target"""
    group = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, group=None, **kwargs):

        super().__init__(**kwargs)

        if group is not None:
            self.group = group


class ProcessPairingConstraint(PairingConstraint, ProcessConstraint, BaseObject):
    """A process-pairing-constraint
processes describes the group of processes that should be paired on the target"""
    group = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, group=None, **kwargs):

        super().__init__(**kwargs)

        if group is not None:
            self.group = group


class DataPairingConstraint(PairingConstraint, DataConstraint, BaseObject):
    """A data-pairing-constraint
labels describes the group of labels that should be paired on the target"""
    group = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, group=None, **kwargs):

        super().__init__(**kwargs)

        if group is not None:
            self.group = group


@abstract
class TriggerEvent(EntityEvent):
    """Defines Events to be used in Stimuli as trigger."""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class StimulusEvent(EntityEvent):
    """Describes the event of a stimulus.
It contains only the stimulus but no event type because a stimulus has only one event type."""
    entity = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, entity=None, **kwargs):

        super().__init__(**kwargs)

        if entity is not None:
            self.entity = entity


class ProcessEvent(EntityEvent):
    """Describes the event of a process
eventType: The type of the Event
entity: The process that fires the event (optional)
processingUnit: The processing unit that executes the process when the event is fired (optional)"""
    eventType = EAttribute(eType=ProcessEventType, unique=False, derived=False, changeable=True)
    entity = EReference(ordered=True, unique=True, containment=False, derived=False)
    processingUnit = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, eventType=None, entity=None, processingUnit=None, **kwargs):

        super().__init__(**kwargs)

        if eventType is not None:
            self.eventType = eventType

        if entity is not None:
            self.entity = entity

        if processingUnit is not None:
            self.processingUnit = processingUnit


class ProcessChainEvent(EntityEvent):
    """Describes the event of some process within a process chain
eventType: The type of the Event
entity: The process that fires the event (optional)
processingUnit: The processing unit that executes the process when the event is fired (optional)"""
    eventType = EAttribute(eType=ProcessEventType, unique=False, derived=False, changeable=True)
    entity = EReference(ordered=True, unique=True, containment=False, derived=False)
    processingUnit = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, eventType=None, entity=None, processingUnit=None, **kwargs):

        super().__init__(**kwargs)

        if eventType is not None:
            self.eventType = eventType

        if entity is not None:
            self.entity = entity

        if processingUnit is not None:
            self.processingUnit = processingUnit


class SemaphoreEvent(EntityEvent):
    """Describes the event of a semaphore access
eventType: The type of event
entity: The accessed semaphore that fires the event (optional)
runnable: The runnable that accesses the semaphore (optional)
process: The process that accesses the semaphore (optional)
processingUnit: The processing unit that executes the process/runnable that accesses the semaphore (optional)"""
    eventType = EAttribute(eType=SemaphoreEventType, unique=False, derived=False, changeable=True)
    entity = EReference(ordered=True, unique=True, containment=False, derived=False)
    runnable = EReference(ordered=True, unique=True, containment=False, derived=False)
    process = EReference(ordered=True, unique=True, containment=False, derived=False)
    processingUnit = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, eventType=None, entity=None, runnable=None, process=None, processingUnit=None, **kwargs):

        super().__init__(**kwargs)

        if eventType is not None:
            self.eventType = eventType

        if entity is not None:
            self.entity = entity

        if runnable is not None:
            self.runnable = runnable

        if process is not None:
            self.process = process

        if processingUnit is not None:
            self.processingUnit = processingUnit


class ComponentEvent(EntityEvent):
    """Describes the event of a component
eventType: The type of event
entity: The component that fires the event (optional)"""
    eventType = EAttribute(eType=ComponentEventType, unique=False, derived=False, changeable=True)
    entity = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, eventType=None, entity=None, **kwargs):

        super().__init__(**kwargs)

        if eventType is not None:
            self.eventType = eventType

        if entity is not None:
            self.entity = entity


class ProcessingUnit(HwModule, HwDestination, HwPathElement):

    definition = EReference(ordered=True, unique=True, containment=False, derived=False)
    accessElements = EReference(ordered=True, unique=True,
                                containment=True, derived=False, upper=-1)
    caches = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, definition=None, accessElements=None, caches=None, **kwargs):

        super().__init__(**kwargs)

        if definition is not None:
            self.definition = definition

        if accessElements:
            self.accessElements.extend(accessElements)

        if caches:
            self.caches.extend(caches)


class ModeValueCondition(ModeValue, ModeCondition):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

    def isSatisfiedBy(self, context=None):

        raise NotImplementedError('operation isSatisfiedBy(...) not yet implemented')


@abstract
class Process(AbstractProcess, IExecutable):
    """Generalizes interrupt service routines and tasks"""
    stimuli = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, stimuli=None, **kwargs):

        super().__init__(**kwargs)

        if stimuli:
            self.stimuli.extend(stimuli)


class DerivedRunnablecalls(EDerivedCollection):
    pass


class DerivedReferringcomponents(EDerivedCollection):
    pass


class Runnable(AbstractMemoryElement, IExecutable, INamespaceMember):
    """Smallest allocatable unit, which provides additional (optional) attributes for allocation algorithms."""
    callback = EAttribute(eType=EBoolean, unique=False, derived=False,
                          changeable=True, default_value='false')
    service = EAttribute(eType=EBoolean, unique=False, derived=False,
                         changeable=True, default_value='false')
    asilLevel = EAttribute(eType=ASILType, unique=False, derived=False, changeable=True)
    executionCondition = EReference(ordered=True, unique=True, containment=True, derived=False)
    parameters = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    activations = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    section = EReference(ordered=True, unique=True, containment=False, derived=False)
    runnableCalls = EReference(ordered=True, unique=True, containment=False,
                               derived=True, upper=-1, transient=True, derived_class=DerivedRunnablecalls)
    referringComponents = EReference(ordered=True, unique=True, containment=False,
                                     derived=True, upper=-1, transient=True, derived_class=DerivedReferringcomponents)

    def __init__(self, *, executionCondition=None, parameters=None, activations=None, callback=None, service=None, asilLevel=None, section=None, runnableCalls=None, referringComponents=None, **kwargs):

        super().__init__(**kwargs)

        if callback is not None:
            self.callback = callback

        if service is not None:
            self.service = service

        if asilLevel is not None:
            self.asilLevel = asilLevel

        if executionCondition is not None:
            self.executionCondition = executionCondition

        if parameters:
            self.parameters.extend(parameters)

        if activations:
            self.activations.extend(activations)

        if section is not None:
            self.section = section

        if runnableCalls:
            self.runnableCalls.extend(runnableCalls)

        if referringComponents:
            self.referringComponents.extend(referringComponents)

    def getRunnableItems(self):

        raise NotImplementedError('operation getRunnableItems(...) not yet implemented')

    def getFirstActivation(self):

        raise NotImplementedError('operation getFirstActivation(...) not yet implemented')


class DerivedLabelaccesses(EDerivedCollection):
    pass


class DerivedReferringcomponents(EDerivedCollection):
    pass


class Label(AbstractMemoryElement, IDisplayName, INamespaceMember):
    """Data representation, which can be accessed by run entities."""
    constant = EAttribute(eType=EBoolean, unique=False, derived=False,
                          changeable=True, default_value='false')
    bVolatile = EAttribute(eType=EBoolean, unique=False, derived=False,
                           changeable=True, default_value='false')
    dataStability = EAttribute(eType=LabelDataStability, unique=False,
                               derived=False, changeable=True)
    stabilityLevel = EAttribute(eType=DataStabilityLevel, unique=False,
                                derived=False, changeable=True)
    dataType = EReference(ordered=True, unique=True, containment=True, derived=False)
    section = EReference(ordered=True, unique=True, containment=False, derived=False)
    labelAccesses = EReference(ordered=True, unique=True, containment=False,
                               derived=True, upper=-1, transient=True, derived_class=DerivedLabelaccesses)
    referringComponents = EReference(ordered=True, unique=True, containment=False,
                                     derived=True, upper=-1, transient=True, derived_class=DerivedReferringcomponents)

    def __init__(self, *, dataType=None, constant=None, bVolatile=None, dataStability=None, stabilityLevel=None, section=None, labelAccesses=None, referringComponents=None, **kwargs):

        super().__init__(**kwargs)

        if constant is not None:
            self.constant = constant

        if bVolatile is not None:
            self.bVolatile = bVolatile

        if dataStability is not None:
            self.dataStability = dataStability

        if stabilityLevel is not None:
            self.stabilityLevel = stabilityLevel

        if dataType is not None:
            self.dataType = dataType

        if section is not None:
            self.section = section

        if labelAccesses:
            self.labelAccesses.extend(labelAccesses)

        if referringComponents:
            self.referringComponents.extend(referringComponents)


class DerivedChannelaccesses(EDerivedCollection):
    pass


class Channel(AbstractMemoryElement, IDisplayName, INamespaceMember):

    defaultElements = EAttribute(eType=EInt, unique=False, derived=False,
                                 changeable=True, default_value='0')
    maxElements = EAttribute(eType=EInt, unique=False, derived=False,
                             changeable=True, default_value='0')
    elementType = EReference(ordered=True, unique=True, containment=True, derived=False)
    channelAccesses = EReference(ordered=True, unique=True, containment=False,
                                 derived=True, upper=-1, transient=True, derived_class=DerivedChannelaccesses)

    def __init__(self, *, elementType=None, defaultElements=None, maxElements=None, channelAccesses=None, **kwargs):

        super().__init__(**kwargs)

        if defaultElements is not None:
            self.defaultElements = defaultElements

        if maxElements is not None:
            self.maxElements = maxElements

        if elementType is not None:
            self.elementType = elementType

        if channelAccesses:
            self.channelAccesses.extend(channelAccesses)


class Composite(Component, ISystem):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DerivedExplicittriggers(EDerivedCollection):
    pass


class CustomEvent(TriggerEvent):

    eventType = EAttribute(eType=EString, unique=False, derived=False, changeable=True)
    explicitTriggers = EReference(ordered=True, unique=True, containment=False,
                                  derived=True, upper=-1, transient=True, derived_class=DerivedExplicittriggers)

    def __init__(self, *, eventType=None, explicitTriggers=None, **kwargs):

        super().__init__(**kwargs)

        if eventType is not None:
            self.eventType = eventType

        if explicitTriggers:
            self.explicitTriggers.extend(explicitTriggers)


class RunnableEvent(TriggerEvent):
    """Describes the event of a runnable
eventType: The type of event
entity: The runnable that fires the event (optional)
process: The process that executes the runnable (optional)
processingUnit: The processing unit that executes the runnable (executes the process that calls the runnable) (optional)"""
    eventType = EAttribute(eType=RunnableEventType, unique=False, derived=False, changeable=True)
    entity = EReference(ordered=True, unique=True, containment=False, derived=False)
    process = EReference(ordered=True, unique=True, containment=False, derived=False)
    processingUnit = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, eventType=None, entity=None, process=None, processingUnit=None, **kwargs):

        super().__init__(**kwargs)

        if eventType is not None:
            self.eventType = eventType

        if entity is not None:
            self.entity = entity

        if process is not None:
            self.process = process

        if processingUnit is not None:
            self.processingUnit = processingUnit


class LabelEvent(TriggerEvent):
    """Describes the event of a label access
eventType: The type of event
entity: The accessed label that fires the event (optional)
runnable: The runnable that accesses the label (optional)
process: The process that accesses the label (optional)"""
    eventType = EAttribute(eType=LabelEventType, unique=False, derived=False, changeable=True)
    entity = EReference(ordered=True, unique=True, containment=False, derived=False)
    runnable = EReference(ordered=True, unique=True, containment=False, derived=False)
    process = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, eventType=None, entity=None, runnable=None, process=None, **kwargs):

        super().__init__(**kwargs)

        if eventType is not None:
            self.eventType = eventType

        if entity is not None:
            self.entity = entity

        if runnable is not None:
            self.runnable = runnable

        if process is not None:
            self.process = process


class ModeLabelEvent(TriggerEvent):
    """Describes the event of a mode label access
eventType: The type of event
entity: The accessed mode label that fires the event
runnable: The runnable that accesses the mode label (optional)
process: The process that accesses the mode label (optional)"""
    eventType = EAttribute(eType=ModeLabelEventType, unique=False, derived=False, changeable=True)
    entity = EReference(ordered=True, unique=True, containment=False, derived=False)
    runnable = EReference(ordered=True, unique=True, containment=False, derived=False)
    process = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, eventType=None, entity=None, runnable=None, process=None, **kwargs):

        super().__init__(**kwargs)

        if eventType is not None:
            self.eventType = eventType

        if entity is not None:
            self.entity = entity

        if runnable is not None:
            self.runnable = runnable

        if process is not None:
            self.process = process


class ChannelEvent(TriggerEvent):
    """Describes the event of a channel access
eventType: The type of event
entity: The accessed channel that fires the event (optional)
runnable: The runnable that accesses the label (optional)
process: The process that accesses the label (optional)"""
    eventType = EAttribute(eType=ChannelEventType, unique=False, derived=False, changeable=True)
    entity = EReference(ordered=True, unique=True, containment=False, derived=False)
    runnable = EReference(ordered=True, unique=True, containment=False, derived=False)
    process = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, eventType=None, entity=None, runnable=None, process=None, **kwargs):

        super().__init__(**kwargs)

        if eventType is not None:
            self.eventType = eventType

        if entity is not None:
            self.entity = entity

        if runnable is not None:
            self.runnable = runnable

        if process is not None:
            self.process = process


class Task(Process):
    """Schedulable entity, which is managed by the OS. An instance of a Task is mapped to exactly one core
and includes the direct representation of all abstractions."""
    preemption = EAttribute(eType=Preemption, unique=False, derived=False, changeable=True)
    multipleTaskActivationLimit = EAttribute(
        eType=EInt, unique=False, derived=False, changeable=True, default_value='0')

    def __init__(self, *, preemption=None, multipleTaskActivationLimit=None, **kwargs):

        super().__init__(**kwargs)

        if preemption is not None:
            self.preemption = preemption

        if multipleTaskActivationLimit is not None:
            self.multipleTaskActivationLimit = multipleTaskActivationLimit


class ISR(Process):
    """Interrupt service routine"""
    category = EAttribute(eType=ISRCategory, unique=False, derived=False, changeable=True)

    def __init__(self, *, category=None, **kwargs):

        super().__init__(**kwargs)

        if category is not None:
            self.category = category
